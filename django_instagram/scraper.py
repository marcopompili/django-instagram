"""
Created on 04/sep/2016

@author: Marco Pompili
"""

from socket import error as socket_error
from lxml import html
import requests
from requests.exceptions import ConnectionError, HTTPError
import json
import logging

SCRIPT_JSON_PREFIX = 18
SCRIPT_JSON_DATA_INDEX = 21


def instagram_scrap_profile(username, headers):
    """
    Scrap an instagram profile page
    :param username:
    :param headers:
    :return:
    """
    try:
        url = "https://www.instagram.com/{}/".format(username)
        page = requests.get(url, headers={
            'User-Agent': headers['User-Agent'],
            'Accept': headers['Accept']
        })
        # Raise error for 404 cause by a bad profile name
        page.raise_for_status()
        return html.fromstring(page.content)
    except HTTPError:
        logging.exception('user profile "{}" not found'.format(username))
    except (ConnectionError, socket_error) as e:
        logging.exception("instagram.com unreachable")


def instagram_profile_js(username, headers):
    """
    Retrieve the script tags from the parsed page.
    :param username:
    :param headers:
    :return:
    """
    try:
        tree = instagram_scrap_profile(username, headers)
        return tree.xpath('//script')
    except AttributeError:
        logging.exception("scripts not found")
        return None


def instagram_profile_json(username, headers):
    """
    Get the JSON data string from the scripts.
    :param username:
    :param headers:
    :return:
    """
    scripts = instagram_profile_js(username, headers)
    source = None

    if scripts:
        for script in scripts:
            if script.text:
                if script.text[0:SCRIPT_JSON_PREFIX] == "window._sharedData":
                    source = script.text[SCRIPT_JSON_DATA_INDEX:-1]

    return source


def instagram_profile_obj(username, headers):
    """
    Retrieve the JSON from the page and parse it to a python dict.
    :param username:
    :param headers:
    :return:
    """
    json_data = instagram_profile_json(username, headers)
    return json.loads(json_data) if json_data else None
