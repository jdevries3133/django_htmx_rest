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

from types import SimpleNamespace
from unittest.mock import patch

import pytest

from .test_negotiator import get_request
from htmx_rest.renderers import HTMXPartialTemplateRenderer


@pytest.fixture
def prepared_renderer():
    renderer = HTMXPartialTemplateRenderer()
    renderer.template_name = 'tests/partial.html'
    return renderer


@pytest.fixture
def expected_html():
    return """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTMX Partial</title>
  </head>
  <body>
    <h1>Htmx template:</h1>
    <div style="border: 1px solid black; padding: 10px; margin: 10px;">
      <div>
  <h1>Hello, world!</h1>
</div>

    </div>
  </body>
</html>"""


@pytest.fixture
def expected_partial():
    return """<div>
  <h1>Hello, world!</h1>
</div>
"""

def test_normal_returns_partial(prepared_renderer, get_request, expected_html):
    res = prepared_renderer.render({'message': 'Hello, world!'}, 'text/html', {
        'view': 'foo view',
        'request': get_request,
        'response': SimpleNamespace(exception=False, template_name=prepared_renderer.template_name)
    })
    assert res == expected_html


def test_hx_request_returns_partial(prepared_renderer, get_request, expected_partial):
    with patch('htmx_rest.renderers.is_hx_request', return_value=True):
        res = prepared_renderer.render({'message': 'Hello, world!'}, 'text/html', {
            'view': 'foo view',
            'request': get_request,
            'response': SimpleNamespace(exception=False, template_name=prepared_renderer.template_name)
        })
        assert res == expected_partial
