import pandas as pd

FILES = ['one_adv.csv', 'two_adv.csv', 'three_adv.csv', 'four_adv.csv', 'five_adv.csv']


def get_adv(times, col):
    """
    :param times: int - 300 if 5min advantage is requested, 1200 if 12min, 1500 if 20min.
    :param col: str - "rad_gold_adv" if gold advantage is requested, "rad_xp_adv" if experience.
    :return: pandas.DataFrame containing a particular advantage info for each match.

    This function is used by the other function get_df below
    """

    final_df = pd.DataFrame()

    for f in FILES:
        filename = 'data/50k_matches/gold_xp/{}'.format(f)

        data = pd.read_csv(filename)
        data = data[data['times'] == times]
        df = data[['match_id', 'times', col]]

        final_df = final_df.append(df, ignore_index=True)

    return final_df


def get_df(times):
    """
    :param times: int - 300 if 5min advantage is requested, 1200 if 12min, 1500 if 20min.
    :return: pandas.DataFrame containing all needed info with a specific time advantage for each match.

    Main function for obtaining data
    """

    df_picks = pd.read_csv('data/50k_matches/match_picks.csv')
    df_gold5 = get_adv(times, 'rad_gold_adv')
    df_xp5 = get_adv(times, 'rad_xp_adv')

    match_winner = pd.read_csv('data/50k_matches/match_winner.csv', header=0)
    match_winner.radiant_win = match_winner.radiant_win.astype(int)

    joined = df_gold5.merge(df_xp5, on=['match_id', 'times']).merge(match_winner, on='match_id') \
        .merge(df_picks, on='match_id')

    return joined
