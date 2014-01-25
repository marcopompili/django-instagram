django-instagram
================

Django Instagram application based on the python-instagram API.

Requirements
------------
- [Django 1.5](https://www.djangoproject.com/)
- [Python Instagram API](https://github.com/Instagram/python-instagram)


Installation
------------
Install django from your favourite package system if you can find it. Or you can use pip for installing python packages that are not listed in the package system of your distribution:
- Install the python-instagram API.
```
pip install python-instagram
```
- Install the django-instagram.

After you cloned the repository, to install this python application you can use the pip command to install local applications like this:
```
pip -e install django-instagram
```

Configuration
-------------
Add the application to INSTALLED_APPS:
```python
INSTALLED_APPS = (... 'django_instagram' ...)
```

Then go to the administration and click on "Get Access Token" to (of course) receive your access token from Instagram. Then copy it to the configuration field and save. Remember to be logged in with the Instagram account that you want to get the access token for.

Usage
-----
After you are done with this, you can use the tags who need user access to Instagram, like:
```
{% instagram_recent_media %}
```
This tag will give you a context variable called: 'recent_media'

To get instagram popular media you don't need an access token instead, so you can ignore the last configuration step above.
```
{% instagram_popular_media %}
```
This tag will give you a context variable callde: 'popular_media'

There's also another inclusion tag that includes an example of how to parse instagram data:
```
{% instagram_popular_media_box %}
```
