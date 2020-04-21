from match import Match
from new724 import get_match_ids
from match_data_functions import check_match_validity
from win_rate import win_rates_by_picks
from write_csv import write_csv_from_list
import time

start = time.time()

ids = get_match_ids('data/Dataset 2-10-2020 (all mmr).csv', 200)

data = []

for id in ids:

    match_data = check_match_validity(id)

    if match_data:
        m = Match(match_data)
        match_id = m.get_match_id()
        picks = m.get_picks_ids()
        win_rates = win_rates_by_picks(picks)
        score = m.get_score()
        lh = m.get_last_hits()
        rw = 1 if m.get_radiant_win() else 0

        res = [sum(i) / 5 for i in win_rates]

        picks_names = m.get_picks_names()
        radiant, dire = picks_names[0], picks_names[1]

        d = [match_id, radiant, dire, rw, score, lh, res[0], res[1]]
        data.append(d)

header = ['Match ID', 'Radiant pick', 'Dire pick', 'Radiant Win', 'Score', 'Last hits', 'radiant win %', 'dire win %']

write_csv_from_list(data, header, 'all_mmr_stats.csv')

print(time.time() - start)
