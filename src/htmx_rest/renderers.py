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


from rest_framework.renderers import TemplateHTMLRenderer

from .util import is_hx_request


# TODO: it would be awesome if there was a cool BrowsableAPIRenderer 2.0
# for this drf-htmx integration where you can also browse your views as
# web components alongside the json.


DUMMY_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTMX Partial</title>
  </head>
  <body>
    <h1>Htmx template:</h1>
    <div style="border: 1px solid black; padding: 10px; margin: 10px;">
      {}
    </div>
  </body>
</html>"""


class HTMXPartialTemplateRenderer(TemplateHTMLRenderer):
    """Will send the partial page when the `Hx-Request` header is set to true.
    Otherwise, it will wrap the partial content in a dummy html template.
    """

    def render(self, *a, **kw):
        content = super().render(*a, **kw)

        if is_hx_request(a[2]["request"]):
            return content

        return DUMMY_TEMPLATE.format(content)
