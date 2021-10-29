# Copyright (c) John DeVries
# All rights reserved.

# This code is licensed under the MIT License.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files(the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and / or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions :

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from rest_framework.negotiation import DefaultContentNegotiation
from rest_framework.renderers import BrowsableAPIRenderer

from .util import is_hx_request


class HtmxContentNegotiator(DefaultContentNegotiation):
    def select_renderer(self, request, renderers, format_suffix=None):
        """In the presence of a `HX-Request: true` header, return html content,
        and avoid using the BrowsableAPIRenderer, which is the default for
        html content types.
        """
        if is_hx_request(request):
            for renderer in renderers:
                if "text/html" in renderer.media_type and not isinstance(
                    renderer, BrowsableAPIRenderer
                ):
                    return (renderer, renderer.media_type)
            raise ValueError(
                "no renderer_class capable of rendering html (not including "
                "the BrowsableAPIRenderer) was provided."
            )

        return super().select_renderer(request, renderers, format_suffix)
