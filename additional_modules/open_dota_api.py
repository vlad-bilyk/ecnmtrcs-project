import requests

key = "3b8b4962-1674-449e-8a5e-b6a500f7b6bb"


def get_match_details(match_id):
    """
    :param match_id: int
    :return: dict
    Returns the request result of a particular match details
    """
    url = 'https://api.opendota.com/api/matches/{}'.format(match_id)

    result = requests.get(url).json()

    return result


def get_hero_vs_hero_stats(heroA_id, heroB_id):
    """
    :param heroA_id: int
    :param heroB_id: int
    :return: list
    Return the request result of stats of matches played between two heroes
    """
    url = "https://api.opendota.com/api/findMatches?teamA={}&teamB={}".format(heroA_id, heroB_id)
    json_data = requests.get(url).json()

    matches_played = len(json_data)
    won = sum([i['teamawin'] for i in json_data])

    return [matches_played, won]
