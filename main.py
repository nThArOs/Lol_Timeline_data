import numpy as np
import matplotlib.pyplot as plt
import pathlib
import pandas as pd
import seaborn as sns
import tensorflow as tf
import time
from tensorflow import keras
from pprint import pprint as pp


from riotwatcher import LolWatcher, ApiError


lol_watcher = LolWatcher('RGAPI-b5c52d42-deef-4af8-a64d-d3c2bc0d5b95')
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
ele = 0
for list in frames:
    #print(ele)
    #pp(list['participantFrames'].keys())
    ele = ele+1
    if '1' in list['participantFrames'].keys():
        print(list['participantFrames']['1'])






#print(data)
#df = pd.DataFrame.from_dict(timelime_data)
#df.to_csv('datatime.csv')





