================
django-instagram
================

A Django application based on the python-instagram API. It allows to use some
template tags to display content from Instagram.

------------
Requirements
------------

* `Django >= 1.6 <https://www.djangoproject.com/>`_
* `Python Instagram API <https://github.com/Instagram/python-instagram>`_

------------
Installation
------------

Install django from your favourite linux packaging system if you can find it.
Or you can use pip for installing python packages that are
not listed in the package system of your distribution:

Use pip to install Django Instagram:

.. code-block:: bash

  pip install django-instagram

Pip should take care of the package dependencies for Django Instagram.

-------------
Configuration
-------------

Add the application to INSTALLED_APPS:

.. code-block:: python

  INSTALLED_APPS = ('...',
                    'django_instagram',)

Rebuild your application database, this command depends on which
version of Django you are using.

In Django 1.9 (recommended):

.. code-block:: bash

  python manage.py makemigrations django_instagram

Them migrate the db:

.. code-block:: bash

  python manage.py migrate

Go to the Django Instagram administration panel and click on "Get
Access Token" button to receive your access token from Instagram.
Then copy and paste it to the configuration field and save.

Remember to be logged in with the Instagram account that you want
to get the access token for.

-----
Usage
-----

After you are done with this, you can use the tags who need user
access to Instagram, this tag will give you a context variable
called: 'recent_media', you can display the data contained in
the recent_media list like this:

.. code-block:: html

  {% load instagram_client %}

  {% instagram_recent_media count=6 %}

  <div id="django_recent_media_wall">
    {% for media in recent_media %}
      <div class="django_instagram_media_wall_item">
        <a href="{{ media.link }}" target="_blank" title="{{ media.caption.text }}">
          <img src="{{ media|thumbnail }}"/>
          <span>{{ media.caption.text }}</span>
        </a>
      </div>
    {% endfor %}
  </div>

To get Instagram popular media you don't need an access token
instead, so you can ignore the last configuration step above.

.. code-block:: html

  {% load instagram_client %}

  {% instagram_popular_media count=10 %}
  <div id="django_instagram_media_wall">
    {% for media in popular_media %}
      <div class="django_instagram_media_wall_item">
        <a href="{{ media.link }}" target="_blank" title="{{ media.caption.text }}">
          <img src="{{ media|standard_size }}"/>
          <span>{{ media.caption.text }}</span>
        </a>
      </div>
    {% endfor %}
  </div>

This tag will give you a context variable called: 'popular_media'

There are also two inclusion tags that includes an example of
how to parse data from Instagram, you can also use them like
this:

.. code-block:: html

  {% load instagram_client %}

  <h1>Instagram media wall</h1>
  {% instagram_recent_media_wall %}

  <h1>Instagram sliding box</h1>
  {% instagram_recent_media_box %}

-------
Filters
-------

As you may have noticed some filters can be used for sizing
the pictures, here is the list of the usable fitlers:

For standard size:

.. code-block:: html

  {% for media in recent_media %}
  ...
  <img src="{{ media|standard_size }}"/>
  ...
  {% endfor %}

For low resolution images:

.. code-block:: html

  {% for media in recent_media %}
  ...
  <img src="{{ media|low_resolution }}"/>
  ...
  {% endfor %}

For thumbnail size:

.. code-block:: html

  {% for media in recent_media %}
  ...
  <img src="{{ media|thumbnail }}"/>
  ...
  {% endfor %}

--------
Releases
--------

* 0.1.1 Numerous bug fixes, better documentation.
* 0.1.0 Work in progress version.
