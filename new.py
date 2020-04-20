from data_functions import *
from match import Match
from get_data_for_hero import get_matches_ids_by_hero


def predict_match(picks_ids, start_at):
    # match_data = check_match_validity(match_id)

    # if not match_data:
    #     return False
    #
    # curr_match = Match(match_data)
    #
    # curr_match_picks = curr_match.get_picks()

    print(picks_ids)

    durations = []

    for side in picks_ids:
        for hero_id in side:

            match_id_list = get_matches_ids_by_hero(hero_id)
            print(match_id_list)

            for match_id in match_id_list:

                match_data = check_match_validity(match_id)
                if match_data:
                    curr_match = Match(match_data)
                    durations.append(curr_match.get_duration())

    print(durations)

    return sum(durations) / 10


picks = Match(check_match_validity(5361650181)).get_picks_ids()

print(predict_match(picks, 5361650181))