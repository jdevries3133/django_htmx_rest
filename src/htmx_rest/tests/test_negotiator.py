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

from unittest.mock import patch

from rest_framework.test import APIRequestFactory
from rest_framework.views import APIView
from rest_framework.renderers import (
    TemplateHTMLRenderer,
    JSONRenderer,
    BrowsableAPIRenderer,
)
import pytest

from htmx_rest.negotiator import HtmxContentNegotiator


@pytest.fixture
def get_request():
    req = APIRequestFactory().get("/", HTTP_ACCEPT="text/html")
    return APIView().initialize_request(req)


@pytest.fixture
def test_renderers():
    """This particular test order is important. The TemplateHTMLRenderer is
    what we want for rendering htmx partials. The JSONRenderer is the
    default, and the BrowsableAPIRenderer is the default for content type
    of text/html"""
    return (
        JSONRenderer(),
        BrowsableAPIRenderer(),
        TemplateHTMLRenderer(),
    )


@pytest.fixture
def default_test_renderers():
    return (
        JSONRenderer(),
        BrowsableAPIRenderer(),
    )


def test_select_renderer_returns_htmx_partial(get_request, test_renderers):
    with patch("htmx_rest.negotiator.is_hx_request", return_value=True):
        neg = HtmxContentNegotiator()
        renderer_cls, content_type = neg.select_renderer(get_request, test_renderers)
        assert isinstance(renderer_cls, TemplateHTMLRenderer)
        assert content_type == "text/html"


def test_select_renderer_returns_browsable_api_for_normal_request(
    get_request, test_renderers
):
    with patch("htmx_rest.negotiator.is_hx_request", return_value=False):
        neg = HtmxContentNegotiator()
        renderer_cls, content_type = neg.select_renderer(get_request, test_renderers)
        assert isinstance(renderer_cls, BrowsableAPIRenderer)
        assert content_type == "text/html"


def test_raises_value_error_if_no_html_renderer_present(
    get_request, default_test_renderers
):
    with patch("htmx_rest.negotiator.is_hx_request", return_value=True):
        neg = HtmxContentNegotiator()
        with pytest.raises(ValueError) as exc:
            neg.select_renderer(get_request, default_test_renderers)
            assert "no renderer_class capable of rendering html" in str(exc.value)
