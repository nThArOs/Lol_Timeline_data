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


lol_watcher = LolWatcher('RGAPI-bf4a1417-6d46-4ed6-9c02-08bfe2f74368')
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
    InfoTimeP1["timestamp"] = minutes
    print(InfoTimeP1)
    d.append(InfoTimeP1)



dd = pd.DataFrame(d)
#print(dd.columns.tolist())
#dd.plot(x ='timestamp', y='totalGold', kind = 'line')
matrix = np.array(dd.xp.values, 'float')
#print(matrix)
X = matrix
X = X / (X * np.max(X))
#print(X)

#print(dd['timestamp'])
#plt.subplots(1)
#dd.plot(x ='timestamp', y=['xp','totalGold'], kind = 'line')
#créer un objet reg lin

modeleReg=LinearRegression()

#créer y et X
xp=dd['xp']
Xre = np.reshape(xp,(-1, 2))
#xpp = dd['xp'].values.reshape((13,2))
print(Xre)
print(Xre.shape)
gold=dd['totalGold']
zime = dd['timestamp']
res = linregress(Xre,zime)
print(res)


model = LinearRegression()
model.fit(xp,zime)
#model = LinearRegression().fit(xp, zime)
#r_sq = model.score(xpp, zime)
#print(r_sq)


plt.rcParams['figure.figsize']=(10, 6)
fig,ax = plt.subplots()
font_used={'fontname':'pristina', 'color':'Black'}
ax.set_ylabel('timestamp',fontsize=20,**font_used)
ax.set_xlabel('xp',fontsize=20,**font_used)
plt.plot(dd['timestamp'],dd['xp'], (res.intercept + res.slope )* dd['xp'])

plt.show()
#plt.subplots(2)
#plt.plot(dd['timestamp'], matrix)
#plt.plot(matrix, dd['timestamp'])

plt.show()

#print(data)
#df = pd.DataFrame.from_dict(timelime_data)
#df.to_csv('datatime.csv')





