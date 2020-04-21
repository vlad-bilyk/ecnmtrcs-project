# useless file

import csv
import json
import math

import requests

from match_data_functions import check_match_validity, get_last_match_ids, get_hero
from write_csv import write_csv_from_dict

key = "0E51DE6A17DA1683650DC1EEACAD43DE"


# LATEST_MATCH_ID = 5363837619


# def get_more_last_match_ids_for_hero(h_id, amount=100):
#     last = LATEST_MATCH_ID
#     last_ids = []
#
#     n = math.ceil(amount / 100)
#     for j in range(0, n):
#         new_ids = get_last_match_ids(matches_requested=100, start_match_id=last, hero_id=h_id)[1:]
#         print(new_ids)
#         last = new_ids[-1]
#         last_ids += new_ids
#         print(len(last_ids))
#
#     return last_ids


def get_matches_ids_by_hero(hero_id, matches_requested=100, skill=0,):
    url = "https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/" \
          "?key={}&matches_requested={}&hero_id={}&min_players=10&skill={}" \
        .format(key, matches_requested, hero_id, skill)

    # print(url)

    id_list = [i['match_id'] for i in requests.get(url).json()['result']['matches']]

    return id_list


def hero_stats_by_match_ids(hero_id, id_list):
    matches = 0
    wins = 0

    for i in id_list:
        match_data = check_match_validity(i)

        if not match_data:
            continue

        matches += 1

        radiant_win = match_data['result']['radiant_win']
        match_picks = get_match_picks1(match_data)
        hero_name = get_hero(hero_id)

        if radiant_win and hero_name in match_picks[0]:
            wins += 1

    return matches, wins


# results = dict()
#
# with open('data/heroes.json', 'r') as f:
#     for i in json.load(f)['result']['heroes'][:5]:
#         hero_name = i['name']
#         hero_id = i['id']
#         results[hero_name] = hero_stats_by_match_ids(hero_id, get_matches_ids_by_hero(hero_id))
#         print(hero_name)
#         print(results[hero_name])
#
# write_csv_from_dict(results, 'every_hero_data.csv')
