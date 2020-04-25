import json


def radiant_win_rate_by_pick(picks_ids):
    """
    :param picks_ids: list of two lists, each containing hero_ids that were picked in a match
    :return: float - win rate for radiant pick against the dire pick

    This function calculates the average of win rates of each radiant hero against the dire pick.
    """
    res = 0

    rad = picks_ids[0]
    dire = picks_ids[1]
    dire.sort()

    with open('data/hero_matchups.json') as file:
        json_data = json.load(file)

    for r in rad:

        matchups = json_data[str(r)]

        win_rate = 0
        for enemy_id in dire:
            values = matchups[str(enemy_id)]
            win_rate += values[1] / values[0]

        avg_wr = round(win_rate / 5, 3)
        res += avg_wr

    return round(res / 5, 3)
