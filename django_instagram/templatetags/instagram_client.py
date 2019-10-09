"""
Created on 12/dic/2013

@author: Marco Pompili
"""

import logging

from django import template

from sorl.thumbnail import get_thumbnail, delete

from django_instagram import settings
from django_instagram.scraper import instagram_profile_obj

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)

register = template.Library()


def get_profile_media(profile, page=0):
    """
    Parse a generated media object
    :param profile:
    :param page:
    :return:
    """
    try:
        edges = profile['entry_data']['ProfilePage'][page]['graphql']['user']['edge_owner_to_timeline_media']['edges']
        return [edge['node'] for edge in edges]
    except KeyError:
        logger.exception("path to profile media not found")


class InstagramUserRecentMediaNode(template.Node):
    """
    Template node for showing recent media from an user.
    """

    def __init__(self, var_name):
        self.var_name = var_name
        self.username = template.Variable(var_name)

    def render(self, context):
        try:
            profile = instagram_profile_obj(self.username.resolve(context))
        except template.base.VariableDoesNotExist:
            logger.warning(
                " variable name \"{}\" not found in context!"
                " Using a raw string as input is DEPRECATED."
                " Please use a template variable instead!".format(self.var_name)
            )

            profile = instagram_profile_obj(username=self.var_name)

        if profile:
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
