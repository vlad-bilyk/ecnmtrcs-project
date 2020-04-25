from additional_modules.steam_api_match_data import get_hero


class Match:
    """
    Class representing a single match with various methods to get info about the match itself.
    """

    def __init__(self, match_data):
        """
        :param match_data: dict
        """
        self.result = match_data['result']
        self.match_data = match_data

    def get_match_id(self):
        """
        :return: int
        Returns the match_id
        """
        return self.result['match_id']

    def get_picks_ids(self):
        """
        :return: tuple
        Returns a tuple of two lists containing heroes' ids
        """
        players = self.match_data['result']['players']
        radiant_heroes = [i['hero_id'] for i in players[:5]]
        dire_heroes = [i['hero_id'] for i in players[5:]]
        return radiant_heroes, dire_heroes

    def get_picks_names(self):
        """
        :return: list
        Return a list of two lists containing heroes' names
        """
        result = [[], []]
        for side, r in zip(self.get_picks_ids(), result):
            for hero_id in side:
                r.append(get_hero(hero_id))
        return result

    def get_radiant_win(self):
        """
        :return: boolean
        Returns True if radiant won, False if dire did
        """
        return self.result['radiant_win']

    def get_duration(self):
        """
        :return: int
        Returns the duration of a match in seconds
        """
        return self.result['duration']

    def get_score(self):
        """
        :return: int
        Returns the difference between radiant's total kills and dire's
        """
        return self.result['radiant_score'] - self.result['dire_score']

    def get_last_hits(self):
        """
        :return: int
        Return the difference between radiant's total last hits and dire's.
        """
        lh = [i['last_hits'] for i in self.result['players']]
        radiant = sum(lh[:5])
        dire = sum(lh[5:])
        return radiant - dire


if __name__ == "__main__":
    from additional_modules.steam_api_match_data import check_match_validity
    m = Match(check_match_validity(5368701809))
    print(m.get_score())
    print(m.get_last_hits())
