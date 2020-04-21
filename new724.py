import csv
from write_csv import heroes_stats_by_match_ids, write_csv_from_dict


def get_match_ids(filename, amount):
    """
    :param filename: string
    :param amount: int, amount of matches
    :return: list of matches ids
    """
    ids = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for row in lines[1:amount + 1]:
            ids.append(row.strip().split(',')[0])

    return ids


# for f1, f2 in zip(['data/Dataset 2-11-2020 (1-3000mmr).csv', 'data/Dataset 2-11-2020 ( 4700mmr).csv'],
#                   ['low_skill_100matches.csv', 'high_skill_100matches.csv']):
#     ids = get_match_ids(f1, 100)
#     stats = heroes_stats_by_match_ids(ids)
#     write_csv_from_dict(stats, f2)
