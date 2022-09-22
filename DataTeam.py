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
#pp(my_matches)
#420 = queue id = 5V5 RANKED SOLO
versions = lol_watcher.data_dragon.versions_for_region(my_region)
champions_version = versions['n']['champion']
summoner_spells_version=versions['n']['summoner']
items_version=versions['n']['item']
( ... )
current_champ_list = lol_watcher.data_dragon.champions(champions_version)
( ... )
#my_matches = lol_watcher.match.matchlist_by_account(my_region, me['accountId'])
my_matches = lol_watcher.match.matchlist_by_puuid(my_region, me['puuid'])
#pp(my_matches)
match_detail = lol_watcher.match.by_id(my_region, "EUW1_5975277597")
timelime_data = lol_watcher.match.timeline_by_match(my_region, "EUW1_5975277597")

n_games = 100
Games = {}
Game_duration = np.zeros(n_games)
Damage = np.zeros(n_games)
(...)
j = 0
cont = 0
while cont < n_games:
    try:

        last_match = my_matches[cont]
        match_info = lol_watcher.match.by_id(my_region, last_match)
        match_detail = match_info['info']
        pp(match_detail.keys())
        participants = []
        for row in match_detail['participants']:
            #pp(match_detail['participants'])
            participants_row = {}
            participants_row['champion'] = row['championId']
            participants_row['win'] = row['stats']['win']
            participants_row['assists'] = row['stats']['assists']

            participants.append(participants_row)
        Games[j] = pd.DataFrame(participants)
        champ_dict = {}
        for key in static_champ_list['data']:
            row = static_champ_list['data'][key]
        champ_dict[row['key']] = row['id']
        summoners_dict = {}
        for key in static_summoners_list['data']:
            row = static_summoners_list['data'][key]
            summoners_dict[row['key']] = row['id']
        Summoner_name = []
        for row in match_detail['participantIdentities']:
            Summoner_name_row = {}
            Summoner_name_row = row['player']['summonerName']
            Summoner_name.append(Summoner_name_row)
        i = 0

        for row in participants:
            row['championName'] = champ_dict[str(row['champion'])]
            row['Summoner_name'] = Summoner_name[i]
            row['Summoner Spell 1'] = summoners_dict[str(row['spell1'])]
            row['Summoner Spell 2'] = summoners_dict[str(row['spell2'])]
            i += 1

        Games[j] = pd.DataFrame(participants)
        for index, row in Games[j].iterrows():
            if row['Summoner_name'] == '%YOUR SUMMONER NAME%':
                Damage[j] = row['totalDamageDealt']
                Gold[j] = row['goldEarned']
                (...)
        time.sleep(10)
        j += 1
        cont += 1
    except:
        cont += 1
