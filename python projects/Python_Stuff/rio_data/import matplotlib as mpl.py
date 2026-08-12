import matplotlib as mpl
import pandas as pd
import datetime as DT
import numpy as np
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import style
df=pd.read_csv('https://raw.githubusercontent.com/cwkteacher/Data/master/athletes.csv')
now = pd.Timestamp(DT.datetime.now())
df['dob'] = pd.to_datetime(df['dob'])
df['dob'] = df['dob'].where(df['dob'] < now, df['dob'] - np.timedelta64(100, 'Y'))
df['age'] = (now - df['dob']).astype('<m8[Y]')
fig, axs = plt.subplots()
df.groupby("age").age.hist(alpha=0.4, bins=2)
fig.savefig("rio_age.png")