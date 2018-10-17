# coding: utf-8

import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


data = pd.read_csv('./booTweetcount_rs.data', dtype={0: str, 1: int}, parse_dates=[0])

data.set_index('datetime', inplace=True)
data.index = pd.to_datetime(data.index, format='%Y-%m-%d %H:%M:%S')

data.plot()
plt.savefig('booTweetcount_rs.png')

