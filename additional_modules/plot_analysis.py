# This code was used to analyze and plot the impact of gold and xp advantage on the match outcome

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

plt.rc("font", size=14)

sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)


def roundup(x):
    return int(math.ceil(x / 100.0)) * 100


def get_stats(infile, times, col):
    filename = 'data/50k_matches/{}'.format(infile)
    print(filename)
    data = pd.read_csv(filename)
    data = data[data['times'] == times]
    # print(data.head())

    match_winner = pd.read_csv('data/50k_matches/match_winner.csv', header=0)
    joined = data.merge(match_winner, on='match_id', how='left')[:]
    # print(joined.head())
    joined[col] = joined[col].map(lambda x: roundup(x))
    # print(joined.head())

    advs = joined.groupby(col)

    stats = {}
    for i in advs.groups.keys():

        group_stats = advs.get_group(i)
        values = group_stats['radiant_win'].value_counts()
        # print(values)
        try:
            won = values[1]
        except KeyError:
            won = 0
        try:
            lost = values[0]
        except KeyError:
            lost = 0
        stats[i] = [won, lost]

    return stats


def plot_data(stats, col_name, outfile):
    keys, values = list(reversed(list(stats.keys()))), list(reversed(list(stats.values())))

    l = len(keys)
    print('LENGTH: ', l)
    k = 2
    if l > 200:
        k = math.floor(l / 70)

    keys = keys[k - 1::k]
    values = values[k - 1::k]

    font = {'family': 'serif',
            'color': 'black',
            'weight': 'normal',
            'size': 19,
            }

    plt.figure(figsize=(25, 14))

    plt.barh(range(len(keys)), values)
    plt.yticks(range(len(keys)), keys)

    plt.xlabel('Win rate %', fontdict=font)
    plt.ylabel(col_name, fontdict=font)

    plt.savefig('plots/{}'.format(outfile))
    plt.show()


files = ['one_new.csv', 'two_new.csv', 'three_new.csv', 'four_new.csv', 'five_new.csv']
columns = ['rad_gold_adv', 'rad_xp_adv']
columns_names = ['rga', 'rxpa']
full_columns_names = ["Radiant Gold Advantage", "Radiant Experience Advantage"]
times = [300, 720, 1500]
times_names = [5, 12, 20]
skips = [3, 5, 7]

for c, cname, fcname in zip(columns, columns_names, full_columns_names):
    for t, tname, sk in zip(times, times_names, skips):
        stats = {}
        for f in files:
            print(f)
            res = get_stats(f, t, c)

            for i in res:

                if i not in stats:
                    stats[i] = res[i]
                else:
                    stats[i][0] += res[i][0]
                    stats[i][1] += res[i][1]

        sorted_stats = {}
        for key in sorted(stats.keys()):
            sorted_stats[key] = stats[key]
            for i in sorted_stats[key]:
                i = int(i)

        for i in sorted_stats:
            won = sorted_stats[i][0]
            lost = sorted_stats[i][1]
            sorted_stats[i] = won / (won + lost)

        plot_data(sorted_stats, '{} on {}th minute'.format(fcname, tname), '{}{}.png'.format(cname, tname))
