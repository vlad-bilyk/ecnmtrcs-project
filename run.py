from log_reg import run_logreg
from data_obtain import get_df

df = get_df(1500)
x = df[['rad_gold_adv', 'rad_xp_adv', 'rad_win_rate']]
y = df['radiant_win']
run_logreg(x, y)
