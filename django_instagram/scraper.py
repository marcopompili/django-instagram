"""
Created on 04/sep/2016

@author: Marco Pompili
"""

from lxml import html
import requests
import json

SCRIPT_JSON_PREFIX = 18
SCRIPT_JSON_DATA_INDEX = 21

def instagram_scrap_profile(username):
    """
    Scrap an instagram profile page
    :param username:
    :return:
    """
    url = "https://www.instagram.com/{}/".format(username)
    page = requests.get(url)
    return html.fromstring(page.content)


def instagram_profile_js(username):
    """
    Retrieve the script tags from the parsed page.
    :param username:
    :return:
    """
    tree = instagram_scrap_profile(username)
    return tree.xpath('//script')


def instagram_profile_json(username):
    """
    Get the JSON data string from the scripts.
    :param username:
    :return:
    """
    scripts = instagram_profile_js(username)
    source = None

    for script in scripts:
        if script.text:
            if script.text[0:SCRIPT_JSON_PREFIX] == "window._sharedData":
                source = script.text[SCRIPT_JSON_DATA_INDEX:-1]

    return source


def instagram_profile_obj(username):
    """
    Retrieve the JSON from the page and parse it to a python dict.
    :param username:
    :return:
    """
    json_data = instagram_profile_json(username)
    return json.loads(json_data)
