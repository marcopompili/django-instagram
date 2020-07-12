django-instagram
================

A Django application that allows to use some template tags for displaying content
from an Instagram public profile.

Requirements
------------

*   [Django >= 1.11](https://www.djangoproject.com/)
*   [lxml](https://pypi.python.org/pypi/lxml/3.6.4)
*   [requests](https://pypi.python.org/pypi/requests/2.11.1)
*   [sorl-thumbnail](https://github.com/mariocesar/sorl-thumbnail)
*   [Pillow](https://pypi.python.org/pypi/Pillow/3.3.1)

Installation
------------

Install Django with your favourite Linux packaging system or you can use pip
for installing python packages, if Django is not an official package for
your distribution:

```bash
pip install django
```

Use pip to install Django Instagram:

```bash
pip install django-instagram
```

Pip should take care of the package dependencies for Django Instagram.

Configuration
-------------

Add the application to INSTALLED_APPS:

```python
INSTALLED_APPS = (
                  ...
                  'sorl.thumbnail', # required for thumbnail support
                  'django_instagram',)
```

Rebuild your application database, this command depends on which
version of Django you are using.

In Django 2.0 (recommended):

```bash
python manage.py makemigrations django_instagram
```

Them migrate the db:

```bash
python manage.py migrate
```

Usage
-----

The `instagram_user_recent_media` brings into context two objects:
  - `profile`: Contains the who scraped object.
  - `recent_media`: Contains the recent media, like 10 or 12 entries or so.

A Django `urls.py` example using a `TemplateView` View class with a context variable called `instagram_profile_name`:

```python
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html', extra_context={
        "instagram_profile_name": "amd"
    })),
]
```

You can display the data contained in `recent_media` list like this:

```html
<!DOCTYPE html>

{% load instagram_client %}

<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ instagram_profile_name|capfirst }} Instagram feed</title>
</head>
<body>
<h1>{{ instagram_profile_name|capfirst }} Instagram Feed</h1>
<div id="django_recent_media_wall">
    {% instagram_user_recent_media instagram_profile_name %}
    {% for media in recent_media %}
        <div class="django_instagram_media_wall_item">
            <a href="//instagram.com/p/{{ media.shortcode }}" target="_blank">
                <img src="{{ media.thumbnail_src }}"/>
                <span>{{ media.edge_media_to_caption.edges.0.node.text }}</span>
            </a>
        </div>
    {% endfor %}
</div>
<p>Got from instagram</p>
</body>
</html>
```

There are also two inclusion tags that includes an example of
how to parse data from Instagram, you can also use them like
this:

```html
{% load instagram_client %}

<h1>Instagram media wall</h1>
{% instagram_recent_media_wall username="intel" %}

<h1>Instagram sliding box</h1>
{% instagram_recent_media_box username="intel" %}
```

Filters
-------

As you may have noticed some filters can be used for sizing the pictures.
Make sure you have `sorl.thumbnail` in the INSTALLED_APPS to use these.

Here is the list of the usable fitlers:

For standard size:

```html
{% for media in recent_media %}
...
<img src="{{ media.thumbnail_src|standard_size }}"/>
...
{% endfor %}
```

For low resolution images:

```html
{% for media in recent_media %}
...
<img src="{{ media.thumbnail_src|low_resolution }}"/>
...
{% endfor %}
```

For thumbnail size:

```html
{% for media in recent_media %}
...
<img src="{{ media.thumbnail_src|thumbnail }}"/>
...
{% endfor %}
```

Releases
--------
*   0.3.2 Compatibility fix for Django 3.
*   0.3.1 Template tag accepts context variables.
*   0.3.0 Updates to the scraping algorithm.
*   0.2.0 New scraping algorithm, removed Python Instagram.
*   0.1.1 Numerous bug fixes, better documentation.
*   0.1.0 Work in progress version.
