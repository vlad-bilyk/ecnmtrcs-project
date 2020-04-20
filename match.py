from data_functions import get_specific_match_data, get_match_picks_ids, get_match_picks_names


class Match:

    def __init__(self, match_data):
        self.result = match_data['result']
        self.match_data = match_data

    def get_match_id(self):
        return self.result['match_id']

    def get_picks_ids(self):
        return get_match_picks_ids(self.match_data)

    def get_radiant_win(self):
        return self.result['radiant_win']

    def get_duration(self):
        return self.result['duration']

    def get_score(self):
        return self.result['radiant_score'], self.result['dire_score']
