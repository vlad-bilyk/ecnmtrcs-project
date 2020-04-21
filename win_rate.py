from match_data_functions import *
from match import Match
import json
import requests


def win_rates_by_picks(picks_ids):
    """
    :param picks_ids: list of heroes id's in a match
    :return: list of 2 lists (for both teams) containing average win rates for each hero against the other team's heroes
    """

    rev = [picks_ids[1], picks_ids[0]]

    scores = [[], []]

    for allies, enemies, sc in zip(picks_ids, rev, scores):

        enemies.sort()
        for hero_id in allies:

            with open('data/hero_matchups.json') as file:
                json_data = json.load(file)
                matchups = json_data[str(hero_id)]

                win_rate = 0
                for enemy_id in enemies:
                    # print('hero_id: ', hero_id)
                    # print('enemy_id: ', enemy_id)
                    values = matchups[str(enemy_id)]
                    win_rate += values[1] / values[0]

                avg_wr = round(win_rate / 5, 3)
                sc.append(avg_wr)

    return scores



