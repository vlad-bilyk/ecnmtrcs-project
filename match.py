from match_data_functions import get_specific_match_data, get_hero


class Match:

    def __init__(self, match_data):
        """

        """
        self.result = match_data['result']
        self.match_data = match_data

    def get_match_id(self):
        return self.result['match_id']

    def get_picks_ids(self):
        players = self.match_data['result']['players']
        radiant_heroes = [i['hero_id'] for i in players[:5]]
        dire_heroes = [i['hero_id'] for i in players[5:]]
        return radiant_heroes, dire_heroes

    def get_picks_names(self):
        result = [[], []]
        for side, r in zip(self.get_picks_ids(), result):
            for hero_id in side:
                r.append(get_hero(hero_id))
        return result

    def get_radiant_win(self):
        return self.result['radiant_win']

    def get_duration(self):
        return self.result['duration']

    def get_score(self):
        return self.result['radiant_score'] - self.result['dire_score']

    def get_last_hits(self):
        lh = [i['last_hits'] for i in self.result['players']]
        radiant = sum(lh[:5])
        dire = sum(lh[5:])
        return radiant - dire


if __name__ == "__main__":
    from match_data_functions import check_match_validity
    m = Match(check_match_validity(5368701809))
    print(m.get_score())
    print(m.get_last_hits())
