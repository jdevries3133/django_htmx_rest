# This is Just an Idea

There is no code, this README just represents an idea for a minimal library
that, as of now, does not exist.

# django-htmx-rest

> A library for bringing together Django, the Django REST Framework, and htmx.

htmx is a new javascript library that allows you to access modern browser
features directly from HTML, rather than using javascript. [See their docs to
learn more, it is really awesome!](https://htmx.org/docs/)

After learning about htmx, it is natural to realize how htmx can bring Roy
Fielding's idea of REST and HATEOS to life in a new, intuitive, and powerful
way. Although htmx is a frontend library, it implies a fresh look at the old
paradigm for building backend-driven web applications.

Despite all of this being very exciting, sticking htmx into a Django project,
or a Django project with DRF does involve a bit of friction. There are a lack
of design patterns, best practices, and library support. Of course, we can build
vies that "do it all," in the sense of serving JSON alongside htmx-cooperative
html snippets, but doing so with consistency, repeatability, and scalability
is where this library fits in.

# Features

Django and DRF are already tools we know and love. This library aims to
smoothly bring htmx into the mix with a minimal framework and utilities that
are both easy to use and understand.

## HTMX REST Views

We provide thin wrappers around DRF view classes and view function decorators
which allow you to provide an html partial template. When a request comes from
htmx, the template provided will be used to provide a html snippet for htmx.

Otherwise, the view will behave like a DRF view, able to serve up JSON, XML,
et cetera.

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

## Supercharged Content Negotiation

Content negotiation and renders are an awesome part of DRF. This library
extends that functionality to provide the tools needed for supporting htmx as
well. A request from `htmx` directly serves up the html snippet, with the
serialized data being passed into your partial template. A direct browser
request shows the browsable API / component explorer, and other content types
are handled by DRF as expected.
