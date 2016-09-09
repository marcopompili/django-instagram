================
django-instagram
================

A Django application that allows to use some template tags to display content
from an Instagram public profile.

------------
Requirements
------------

* `Django >= 1.6 <https://www.djangoproject.com/>`_
* `lxml <https://pypi.python.org/pypi/lxml/3.6.4>`_
* `requests <https://pypi.python.org/pypi/requests/2.11.1>`_
* `sorl-thumbnail <https://github.com/mariocesar/sorl-thumbnail>`_
* `Pillow <https://pypi.python.org/pypi/Pillow/3.3.1>`_

------------
Installation
------------

Install Django with your favourite linux packaging system or you can use pip
for installing python packages, if Django is not an official package for
your distribution:

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
access to Instagram, this tag will give two context variables
called:

- profile:
- recent_media:

You can display the data contained in recent_media list like this:

.. code-block:: html

  {% load instagram_client %}

  {% instagram_user_recent_media intel %}

  <div id="django_recent_media_wall">
    {% for media in recent_media %}
      <div class="django_instagram_media_wall_item">
        <a href="{{ media.display_src }}" target="_blank" title="{{ media.caption }}">
          <img src="{{ media.thumbnail_src }}"/>
          <span>{{ media.caption }}</span>
        </a>
      </div>
    {% endfor %}
  </div>

There are also two inclusion tags that includes an example of
how to parse data from Instagram, you can also use them like
this:

.. code-block:: html

  {% load instagram_client %}

  <h1>Instagram media wall</h1>
  {% instagram_recent_media_wall username="intel" %}

  <h1>Instagram sliding box</h1>
  {% instagram_recent_media_box username="intel" %}

-------
Filters
-------

As you may have noticed some filters can be used for sizing
the pictures, here is the list of the usable fitlers:

For standard size:

.. code-block:: html

  {% for media in recent_media %}
  ...
  <img src="{{ media.thumbnail_src|standard_size }}"/>
  ...
  {% endfor %}

For low resolution images:

.. code-block:: html

  {% for media in recent_media %}
  ...
  <img src="{{ media.thumbnail_src|low_resolution }}"/>
  ...
  {% endfor %}

For thumbnail size:

.. code-block:: html

  {% for media in recent_media %}
  ...
  <img src="{{ media.thumbnail_src|thumbnail }}"/>
  ...
  {% endfor %}

--------
Releases
--------
* 0.2.0 New scraping algorithm, removed Python Instagram.
* 0.1.1 Numerous bug fixes, better documentation.
* 0.1.0 Work in progress version.
