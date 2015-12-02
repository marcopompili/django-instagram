"""
Created on 12/dic/2013

@author: Marco Pompili
"""

from instagram.client import InstagramAPI

from django import template

from django_instagram.models import InstagramConfiguration

register = template.Library()

DJANGO_INSTAGRAM_CLIENT_ID = "5668831cb13b4876a63fa53fe768927e"
DJANGO_INSTAGRAM_REDIRECT_URI = "http://www.emarcs.net/instagram/"


def instagram_sign_in_with_token():
    token = InstagramConfiguration.objects.first()

    if token is None:
        print("Django Instagram, configuration not found")
        return token
    else:
        return InstagramAPI(access_token=token.app_access_token)


def instagram_get_recent_media(count):
    api = instagram_sign_in_with_token()

    if api:
        recent_media, next_ = api.user_recent_media(count=count)
        return recent_media
    else:
        return None


class InstagramPopularMediaNode(template.Node):
    """
        Template node for displaying the popular media of Instagram.
        The API doesn't need authentication, just basic access.
    """
    def __init__(self, count):
        self.count = count
        self.api = InstagramAPI(client_id=DJANGO_INSTAGRAM_CLIENT_ID)

    def render(self, context):
        popular_media = self.api.media_popular(self.count)

        context['popular_media'] = popular_media

        return ''


@register.tag
def instagram_popular_media(parser, token):
    """
        Tag for getting data about popular media on Instagram.
    """
    try:
        tagname, count = token.split_contents()

        return InstagramPopularMediaNode(count.split('=')[1])
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires a single argument" % token.contents.split()[0]
        )


class InstagramRecentMediaNode(template.Node):
    """
        Template node for showing recent media from an user.
        This functionality needs an access token.
        The access token should be set in the administration interface.

        If no access token is set the process should fail silently,
        so watch out for error messages in the console.
    """

    def __init__(self, count):
        self.count = count

    def render(self, context):
        context['recent_media'] = instagram_get_recent_media(self.count)

        return ''


@register.tag
def instagram_recent_media(parser, token):
    """
        Tag for getting data about recent media of an user.
    """
    try:
        tagname, count = token.split_contents()

        return InstagramRecentMediaNode(count.split('=')[1])
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires a single argument" % token.contents.split()[0]
        )


@register.inclusion_tag('django_instagram/recent_media_box.html')
def instagram_recent_media_box(*args, **kwargs):
    recent_media = instagram_get_recent_media(count=kwargs.get('count', 10))

    return {
        'recent_media': recent_media
    }


@register.inclusion_tag('django_instagram/recent_media_wall.html')
def instagram_recent_media_wall(*args, **kwargs):
    recent_media = instagram_get_recent_media(count=kwargs.get('count', 10))

    return {
        'recent_media': recent_media
    }

@register.filter(name='standard_size')
def instagram_standard_size(value):
    return value.images['standard_resolution'].url


@register.filter(name='low_resolution')
def instagram_low_resolution(value):
    return value.images['low_resolution'].url


@register.filter(name='thumbnail')
def instagram_thumbnail(value):
    return value.images['thumbnail'].url
