import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)


data = pd.read_csv('data/50k_matches/match.csv', header=0)
data = data.dropna()
# print(data.shape)
# print(list(data.columns))
# print(data.head())

# print(data['radiant_win'].value_counts())
#
# sns.countplot(x='radiant_win', data=data, palette='hls')
# plt.show()
# plt.savefig('count_plot')

# rad_win = len(data[data['radiant_win'] == True])
# rad_win_prc = rad_win / 50000
# dire_win_prc = 1 - rad_win_prc

# print(rad_win_prc, dire_win_prc)

# print(data.groupby('radiant_win').mean()['duration'])
#
# pd.crosstab(data.duration, data.radiant_win).plot(kind='bar')
# plt.title('Purchase Frequency for Job Title')
# plt.xlabel('duration')
# plt.ylabel('radiant_win')
# plt.savefig('purchase_fre_job')

# newdata = pd.read_csv('data/50k_matches/one.csv', header=0)
#
# match = pd.read_csv('data/50k_matches/match.csv', header=0)
# df = match[['match_id', 'radiant_win']]
# id = df['match_id']
# print(id)
#
# final = newdata.join(df, on='match_id', how='left')
#
# print(final)
data = pd.read_csv('data/50k_matches/two.csv', header=0)
print(data.header())
