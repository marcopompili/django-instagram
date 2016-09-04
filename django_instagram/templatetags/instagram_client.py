"""
Created on 12/dic/2013

@author: Marco Pompili
"""

from django import template

from sorl.thumbnail import get_thumbnail, delete

from django_instagram import settings
from django_instagram.scraper import instagram_profile_json, instagram_profile_obj

register = template.Library()

def get_profile_media(profile, page = 0):
    """
    Parse a generated media object
    :param profile:
    :param page:
    :return:
    """
    return profile['entry_data']['ProfilePage'][page]['user']['media']['nodes']


class InstagramUserRecentMediaNode(template.Node):
    """
    Template node for showing recent media from an user.
    """

    def __init__(self, username):
        self.username = username

    def render(self, context):
        profile = instagram_profile_obj(username=self.username)
        context['profile'] = profile
        context['recent_media'] = get_profile_media(profile)

        return ''



@register.tag
def instagram_user_recent_media(parser, token):
    """
    Tag for getting data about recent media of an user.
    :param parser:
    :param token:
    :return:
    """
    try:
        tagname, username = token.split_contents()

        return InstagramUserRecentMediaNode(username)
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires a single argument" % token.contents.split()[0]
        )

@register.inclusion_tag('django_instagram/recent_media_box.html')
def instagram_recent_media_box(*args, **kwargs):
    profile = instagram_profile_obj(username=kwargs.get('username'))
    recent_media = get_profile_media(profile)

    return {
        'profile': profile,
        'recent_media': recent_media
    }


@register.inclusion_tag('django_instagram/recent_media_wall.html')
def instagram_recent_media_wall(*args, **kwargs):
    profile = instagram_profile_obj(username=kwargs.get('username'))
    recent_media = get_profile_media(profile)

    return {
        'profile': profile,
        'recent_media': recent_media,
    }


@register.filter(name='standard_size')
def instagram_standard_size(value):
    im = get_thumbnail(value, settings.INSTAGRAM_STANDARD_SIZE, crop='center', quality=90)
    return im.url


@register.filter(name='low_resolution')
def instagram_low_resolution(value):
    im = get_thumbnail(value, settings.INSTAGRAM_LOW_SIZE, crop='center', quality=90)
    return im.url


@register.filter(name='thumbnail')
def instagram_thumbnail(value):
    im = get_thumbnail(value, settings.INSTAGRAM_THUMB_SIZE, crop='center', quality=90)
    return im.url
