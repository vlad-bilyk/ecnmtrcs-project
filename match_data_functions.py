import math

import requests
import json

key = "0E51DE6A17DA1683650DC1EEACAD43DE"

LATEST_MATCH_ID = 5363449253


def get_specific_match_data(match_id):
    url = "http://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v1/?match_id={}&key={}".format(match_id, key)
    # print(url)
    json_data = requests.get(url).json()
    # print(json_data)
    return json_data


def get_last_match_ids(skill=0, matches_requested=100, start_match_id=LATEST_MATCH_ID, hero_id=1):
    url = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?format=json&key={}" \
          "&min_players=10&skill={}&matches_requested={}" \
        .format(key, skill, matches_requested)

    if start_match_id:
        url += "&start_at_match_id={}".format(start_match_id)

    if hero_id:
        url += "&hero_id={}".format(hero_id)

    # print(url)
    json_data = requests.get(url).json()
    ids = [i['match_id'] for i in json_data['result']['matches']]
    return ids


def get_my_last_matces():
    url = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?account_id=76561198060149110&key={}".format(
        key)
    print(url)
    json_data = requests.get(url).json()
    ids = [i['match_id'] for i in json_data['result']['matches']]
    return ids


def get_hero(hero_id):
    with open('data/heroes.json', 'r') as f:
        json_data = json.load(f)
    for i in json_data['result']['heroes']:
        if hero_id == i['id']:
            return i['name']

def check_match_validity(match_id):
    match_data = get_specific_match_data(match_id)

    if match_data['result']['duration'] < 1080:
        return False

    return match_data


# def get_match_picks_ids(match_data):
#     players = match_data['result']['players']
#     radiant_heroes = [i['hero_id'] for i in players[:5]]
#     dire_heroes = [i['hero_id'] for i in players[5:]]
#     return radiant_heroes, dire_heroes


# def get_match_picks_names(picks_ids):
#     radiant_heroes = [get_hero(i) for i in picks_ids[0]]
#     dire_heroes = [get_hero(i) for i in picks_ids[1]]
#     return radiant_heroes, dire_heroes
#
#
# def get_match_heroes(match_data):
#     return [get_hero(i['hero_id'] for i in match_data['result']['players'])]





# def get_match_picks2(match_id):
#     rad_heroes = []
#     dire_heroes = []
#     match = get_specific_match_data(match_id)
#     picks_bans = match['result']['picks_bans']
#
#     for pb in picks_bans:
#
#         if not pb["is_pick"]:
#             continue
#
#         team = pb['team']  # 0 -  radiant, 1 - dire
#         hero_id = pb['hero_id']
#
#         if team:
#             dire_heroes.append(get_hero(hero_id))
#         else:
#             rad_heroes.append(get_hero(hero_id))
#
#     return rad_heroes, dire_heroes

# print(get_match_picks2(5363196921))


# my_ids = get_my_last_matces()

def get_more_last_match_ids(amount=100):
    last = LATEST_MATCH_ID
    last_ids = []

    n = math.ceil(amount / 100)
    for j in range(0, n):
        new_ids = get_last_match_ids(matches_requested=100, start_match_id=last)[1:]
        print(new_ids)
        last = new_ids[-1]
        last_ids += new_ids
        print(len(last_ids))

    return last_ids


print(get_specific_match_data(1955255913))
