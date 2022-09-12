import numpy as np
import matplotlib.pyplot as plt
import pathlib
import pandas as pd
import seaborn as sns
import tensorflow as tf
import time
from tensorflow import keras
from pprint import pprint as pp
from scipy.stats import linregress


from riotwatcher import LolWatcher, ApiError


lol_watcher = LolWatcher('RGAPI-2be5655a-4aff-4073-91b5-2b6e2f74e3b1')
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
pp(frames[2].keys())
#pp(frames[2]['participantFrames'])
#pp(frames[2]['timestamp'])
#pp(frames[2]['events'])
#info = frames['participantsFrames']

#InfoP1 = pd.DataFrame.from_records(frames, index=['participantsFrames']['1'])

etry = pd.DataFrame.from_dict(frames)
#eztry = pd.DataFrame.from_records(frames, index="")
ele = 0
d = []
for list in frames:
    InfoTimeP1 = list['participantFrames']['1']
    timestampe = list['timestamp']
    minutes = (timestampe / (1000 * 60)) % 60
    InfoTimeP1["timestamp"] = timestampe
    print(InfoTimeP1)
    d.append(InfoTimeP1)



dd = pd.DataFrame(d)
print(dd.columns.tolist())
#dd.plot(x ='timestamp', y='totalGold', kind = 'line')
matrix = np.array(dd.xp.values,'float')
print(matrix)
X = matrix
X = X/(np.max(X))
print(X)
#plt.subplots(1)
#dd.plot(x ='timestamp', y=['xp','totalGold'], kind = 'line')
plt.plot(x=dd['timestamp'], y=dd['xp','totalGold'], kind = 'line')

#plt.subplots(2)
plt.plot(dd['timestamp'],matrix)

plt.show()

#print(data)
#df = pd.DataFrame.from_dict(timelime_data)
#df.to_csv('datatime.csv')





