import csv
import json

from match_data_functions import get_more_last_match_ids, check_match_validity, get_hero
from match import Match


def heroes_stats_by_match_ids(id_list):
    zero_list = [0, 0]

    with open('data/heroes.json', 'r') as f:
        hero_picks = dict.fromkeys([i['name'] for i in json.load(f)['result']['heroes']])
        for i in hero_picks:
            hero_picks[i] = zero_list[:]

    print(hero_picks)

    # print(last_ids)

    for i in id_list:
        match_data = check_match_validity(i)

        if not match_data:
            continue

        match = Match(match_data)

        radiant_win = match.get_radiant_win()

        print("id: ", i)
        match_picks = match.get_picks_ids()
        # print(match_picks)

        for side in match_picks:
            # print(side)
            # print(hero_picks)
            for hero_id in side:
                # pr_int(hero)
                # print(hero_picks[hero])
                hero = get_hero(hero_id)
                hero_picks[hero][0] += 1
                if radiant_win:
                    hero_picks[hero][1] += 1
            radiant_win = not radiant_win

    return hero_picks


def write_csv_from_dict(data, filename):
    """

    :param data: dictionary, format ---> hero_name: [times_picked, games_won]
    :param filename: name of the resulting file
    :return: None
    """
    with open('results/{}'.format(filename), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Hero", "Times picked", "Win rate %"])
        for hero in data:
            times_picked = data[hero][0]
            if times_picked > 0:
                win_rate = data[hero][1] / times_picked
            else:
                win_rate = 0
            row = [hero, times_picked, round(win_rate, 2)]
            writer.writerow(row)


def write_csv_from_list(data, header, filename):
    """
    :param data: list of lists of data
    :param header: header of csv file
    :param filename: name of the resulting file
    :return: None
    """
    with open('results/{}'.format(filename), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for row in data:
            writer.writerow(row)
