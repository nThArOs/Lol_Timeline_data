import numpy as np
import matplotlib.pyplot as plt
import pathlib
import pandas as pd
import seaborn as sns
import time
from pprint import pprint as pp
from scipy.stats import linregress
from sklearn.linear_model import LinearRegression
from riotwatcher import LolWatcher, ApiError
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.feature_selection import mutual_info_regression

lol_watcher = LolWatcher('RGAPI-36daa904-8348-486e-983e-e91a4dbe4fdc')
my_region = 'euw1'
my_name = 'ButWhoGonaSTOPme'
me = lol_watcher.summoner.by_name(my_region, my_name)
my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
#420 = queue id = 5V5 RANKED SOLO
my_matches = lol_watcher.match.matchlist_by_puuid(my_region, me['puuid'], 420)
#print(my_matches)
#print(me['puuid'])
match_data = lol_watcher.match.by_id(my_region, "EUW1_5975277597")
timelime_data = lol_watcher.match.timeline_by_match(my_region, "EUW1_5975277597")
data = timelime_data['info']
print(data.keys())
frames = data['frames']
#print(frames)
#pp(frames[2].keys())


etry = pd.DataFrame.from_dict(frames)
ele = 0
d = []
for list in frames:
    InfoTimeP1 = list['participantFrames']['1']
    timestampe = list['timestamp']
    minutes = (timestampe / (1000 * 60)) % 60
    InfoTimeP1["timestamp"] = minutes
    #print(InfoTimeP1)
    d.append(InfoTimeP1)



dd = pd.DataFrame(d)
pp(dd.keys())
"""
#print(dd.columns.tolist())
#dd.plot(x ='timestamp', y='totalGold', kind = 'line')
matrix = np.array(dd.xp.values, 'float')
#print(matrix)
X = matrix
X = X / (X * np.max(X))

xp=dd['xp']
gold=dd['totalGold']
zime = dd['timestamp']
plt.rcParams['figure.figsize']=(10, 6)
fig,ax = plt.subplots()
font_used={'fontname':'pristina', 'color':'Black'}
ax.set_ylabel('timestamp',fontsize=20,**font_used)
ax.set_xlabel('xp',fontsize=20,**font_used)
plt.plot(dd['timestamp'],dd['xp'])

plt.show()
#plt.subplots(2)
#plt.plot(dd['timestamp'], matrix)
#plt.plot(matrix, dd['timestamp'])

plt.show()
"""
#print(data)
#df = pd.DataFrame.from_dict(timelime_data)
#df.to_csv('datatime.csv')





