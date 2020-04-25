# these functions were used in the first stages, but not anymore

import requests
import json

key = "0E51DE6A17DA1683650DC1EEACAD43DE"


def get_specific_match_data(match_id):
    """
    :param match_id: id of a match
    :return: dict - match data
    """
    url = "http://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v1/?match_id={}&key={}".format(match_id, key)
    # print(url)
    json_data = requests.get(url).json()
    # print(json_data)
    return json_data


def get_hero(hero_id):
    """
    :param hero_id: id of a hero
    :return: str - name of a hero
    """
    with open('data/heroes.json', 'r') as f:
        json_data = json.load(f)
    for i in json_data['result']['heroes']:
        if hero_id == i['id']:
            return i['name']


def check_match_validity(match_id):
    """
    :param match_id: id of a match
    return: dict - match data
    """
    match_data = get_specific_match_data(match_id)

    if match_data['result']['duration'] < 1080:
        return False

    return match_data
