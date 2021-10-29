# django-htmx-rest

> A library for bringing together the
> [Django REST Framework](https://www.django-rest-framework.org/)
> and
> [htmx](https://htmx.org/docs/).

htmx is a new javascript library based on Intercooler.js that allows you to
access modern browser features directly from HTML, rather than using
javascript.

This library is super tiny for now, and focuses on providing a framework for
backend patterns that support htmx, like content negotiation and improvements
to DRF's browsable API.

# Features

## Content Negotiation

We extend the default content negotiation behavior of DRF to serve a partial
template in the presence of htmx's `Hx-Request` header. Otherwise, the htmx
partial is wrapped in a full page. This does, however override DRF's
browsable API.

In the future, the plan is to enhance DRF's browsable API, and to serve the
htmx component alongside the browsable data for a request for `text/html`
without the `Hx-Request` header. This would allow the same view to serve
JSON, the htmx partial content, and a full browsable page for developers.
This feature can also include basic frontend development tooling like live
reloading and viewport resizing, like what Storybook and other isolated
UI development tools provide, allowing rapid development of htmx partials.

# Future Features

## New Spin on the Browsable API

With htmx, your browsable API is not just a view into your application data,
but also a sort of storybook for UI components, as expressed by HTMX partials.

If you directly visit a `htmx-rest` view in your browser, you will still be
able to access the DRF browsable API, but you'll also be able to see and
interact with the HTMX component in isolation with live reloading, and basic UI
development tools, like changing the viewport size, and viewing the context
data being passed into the template

Also, to help you browse through all your `htmx-rest` views, our browsable
interface has a sidebar listing all of the `htmx-rest` views in your
application, so you can explore them.

# Setup

First, install the package:

```
pip install django-htmx-rest
```

Then, add put the following in your `settings.py` file:

```python
# settings.py

INSTALLED_APPS = [
    ...
    'htmx_rest'
    ...
]


REST_FRAMEWORK = {

    'DEFAULT_CONTENT_NEGOTIATION_CLASS':
        'htmx_rest.negotiator.HtmxContentNegotiator',

    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',

         # optional, if you want the browsable api
        'rest_framework.renderers.BrowsableAPIRenderer',

        # this or some renderer other than the BrowsableAPIRenderer that can
        # render content_types of `text/html` must be present
        'htmx_rest.renderers.HTMXPartialTemplateRenderer',
    ]
}
```
