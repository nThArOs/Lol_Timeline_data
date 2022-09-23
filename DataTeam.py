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

lol_watcher = LolWatcher('RGAPI-893ad16c-e01a-4611-966b-aeb012c6f70b')
my_region = 'euw1'
my_name = 'ButWhoGonaSTOPme'
me = lol_watcher.summoner.by_name(my_region, my_name)
my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
# pp(my_matches)
# 420 = queue id = 5V5 RANKED SOLO
versions = lol_watcher.data_dragon.versions_for_region(my_region)

champions_version = versions['n']['champion']
summoner_spells_version = versions['n']['summoner']
items_version = versions['n']['item']

current_champ_list = lol_watcher.data_dragon.champions(champions_version)
# my_matches = lol_watcher.match.matchlist_by_account(my_region, me['accountId'])
my_matches = lol_watcher.match.matchlist_by_puuid(my_region, me['puuid'])
# pp(my_matches)
n_games = 100
Games = {}
Game_duration = np.zeros(n_games)
Damage = np.zeros(n_games)
j = 0
cont = 0
d = pd.DataFrame()
while cont < n_games:
    try:

        last_match = my_matches[cont]
        match_info = lol_watcher.match.by_id(my_region, last_match)
        match_detail = match_info['info']

        lol_dataset = []
        lol_dataset_row = {}

        lol_dataset_row['gameId'] = match_detail['gameId']
        lol_dataset_row['gameMode'] = match_detail['gameMode']
        lol_dataset_row['gameVersion'] = match_detail['gameVersion']
        lol_dataset_row['gameStartTimestamp'] = match_detail['gameStartTimestamp']
        lol_dataset_row['gameEndTimestamp'] = match_detail['gameEndTimestamp']
        lol_dataset_row['gameDuration'] = match_detail['gameDuration']
        lol_dataset_row['blueWin'] = match_detail['teams'][0]['win']
        lol_dataset_row['redWin'] = match_detail['teams'][1]['win']
        lol_dataset_row['blueChampion0'] = match_detail['participants'][0]['championName']
        lol_dataset_row['blueChampion1'] = match_detail['participants'][1]['championName']
        lol_dataset_row['blueChampion2'] = match_detail['participants'][2]['championName']
        lol_dataset_row['blueChampion3'] = match_detail['participants'][3]['championName']
        lol_dataset_row['blueChampion4'] = match_detail['participants'][4]['championName']
        lol_dataset_row['redChampion0'] = match_detail['participants'][5]['championName']
        lol_dataset_row['redChampion1'] = match_detail['participants'][6]['championName']
        lol_dataset_row['redChampion2'] = match_detail['participants'][7]['championName']
        lol_dataset_row['redChampion3'] = match_detail['participants'][8]['championName']
        lol_dataset_row['redChampion4'] = match_detail['participants'][9]['championName']

        lol_dataset_row['blueKill'] = match_detail['teams'][0]['objectives']['champion']['kills']
        lol_dataset_row['blueFirstKill'] = match_detail['teams'][0]['objectives']['champion']['first']
        lol_dataset_row['blueBaron'] = match_detail['teams'][0]['objectives']['baron']['kills']
        lol_dataset_row['blueFirstBaron'] = match_detail['teams'][0]['objectives']['baron']['first']
        lol_dataset_row['blueDragon'] = match_detail['teams'][0]['objectives']['dragon']['kills']
        lol_dataset_row['blueFirstDragon'] = match_detail['teams'][0]['objectives']['dragon']['first']
        lol_dataset_row['blueInhibitor'] = match_detail['teams'][0]['objectives']['inhibitor']['kills']
        lol_dataset_row['blueFirstInhibitor'] = match_detail['teams'][0]['objectives']['inhibitor']['first']
        lol_dataset_row['blueRiftHerald'] = match_detail['teams'][0]['objectives']['riftHerald']['kills']
        lol_dataset_row['blueFirstRiftHerald'] = match_detail['teams'][0]['objectives']['riftHerald']['first']
        lol_dataset_row['blueTower'] = match_detail['teams'][0]['objectives']['tower']['kills']
        lol_dataset_row['blueFirstTower'] = match_detail['teams'][0]['objectives']['tower']['first']

        lol_dataset_row['redKill'] = match_detail['teams'][1]['objectives']['champion']['kills']
        lol_dataset_row['redFirstKill'] = match_detail['teams'][1]['objectives']['champion']['first']
        lol_dataset_row['redBaron'] = match_detail['teams'][1]['objectives']['baron']['kills']
        lol_dataset_row['redFirstBaron'] = match_detail['teams'][1]['objectives']['baron']['first']
        lol_dataset_row['redDragon'] = match_detail['teams'][1]['objectives']['dragon']['kills']
        lol_dataset_row['redFirstDragon'] = match_detail['teams'][1]['objectives']['dragon']['first']
        lol_dataset_row['redInhibitor'] = match_detail['teams'][1]['objectives']['inhibitor']['kills']
        lol_dataset_row['redFirstInhibitor'] = match_detail['teams'][1]['objectives']['inhibitor']['first']
        lol_dataset_row['redRiftHerald'] = match_detail['teams'][1]['objectives']['riftHerald']['kills']
        lol_dataset_row['redFirstRiftHerald'] = match_detail['teams'][1]['objectives']['riftHerald']['first']
        lol_dataset_row['redTower'] = match_detail['teams'][1]['objectives']['tower']['kills']
        lol_dataset_row['redFirstTower'] = match_detail['teams'][1]['objectives']['tower']['first']



        #pp(match_detail['teams'])

        """"
        #ArrayofChampofGold
        i = 1
        champList = []
        for i in range(len(match_detail['participants'])):
            i += 1
            champLista = {
                match_detail['participants'][i-1]['championName']: {
                    "goldEarned": match_detail['participants'][i-1]['goldEarned'],
                    "goldSpent": match_detail['participants'][i-1]['goldSpent']}
                }
            champList.append(champLista)           
            if i == len(match_detail['participants']):
                #print(champList)
                lol_dataset_row['champGold'] = champList
        """

        blueMaxGPM = None
        redMaxGPM = None
        m = 0
        for m in range(len(match_detail['participants'])):
            print(m)
            tmpGPM = match_detail['participants'][m-1]['goldPerMinute']
            print(match_detail['participants'][m-1])
            print(tmpGPM)
            m += 1

        #print(blueGPM,blueMaxGPM,redGPM,redMaxGPM)
        lol_dataset.append(lol_dataset_row)
        #print(lol_dataset)
        tmp = pd.DataFrame(lol_dataset)
        d = pd.concat([d, tmp])
        j += 1
        cont += 1
    except:
        cont += 1
#print(d.head())
d.to_csv("lol_data.csv",index=False)