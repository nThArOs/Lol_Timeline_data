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
import builtins

lol_watcher = LolWatcher('RGAPI-baedaf02-ba62-4bb0-9900-4085c17763cb')
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
master = lol_watcher.league.masters_by_queue(my_region,'RANKED_SOLO_5x5')
grandMaster = lol_watcher.league.grandmaster_by_queue(my_region,'RANKED_SOLO_5x5')
chall = lol_watcher.league.challenger_by_queue(my_region,'RANKED_SOLO_5x5')

list_master = master['entries']
list_gm = grandMaster['entries']
list_chall = chall['entries']

#print(list_chall.types)
master = pd.DataFrame.from_dict(list_master)
gm = pd.DataFrame.from_dict(list_gm)
chall = pd.DataFrame.from_dict(list_chall)

lead = [master,gm,chall]
leadboard = pd.concat(lead)
leadboard = leadboard[['leaguePoints','rank','summonerName','wins','losses','hotStreak','veteran','freshBlood','inactive','summonerId']]
leadboard = leadboard.sort_values(by=['leaguePoints'], ascending=False)
leadboard.to_csv("leadboard.csv",index=False)
print(leadboard)
histo_leadboard =
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

        blueMaxGPM = 0
        redMaxGPM = 0
        blueGPM = 0
        redGPM = 0
        blueMaxKill = 0
        blueKill = 0
        redMaxKill = 0
        redKill = 0
        i = 1

        #print(match_detail['participants'][1].keys())
        #print(match_detail['participants'][1])

        #print(match_detail['participants'][1]['wardsPlaced'])
        blueMaxWardsPlaced = max(match_detail['participants'][0:5], key=lambda d: d['wardsPlaced'])
        redMaxWardsPlaced = max(match_detail['participants'][5:10], key=lambda d: d['wardsPlaced'])
        blueSumWardsPlaced = sum(d['wardsPlaced'] for d in match_detail['participants'][0:5])
        redSumWadsPlaced = sum(d['wardsPlaced'] for d in match_detail['participants'][5:10])

        blueMaxWardsKilled = max(match_detail['participants'][0:5], key=lambda d: d['wardsKilled'])
        redMaxWardsKilled = max(match_detail['participants'][5:10], key=lambda d: d['wardsKilled'])
        blueSumWardsKilled = sum(d['wardsKilled'] for d in match_detail['participants'][0:5])
        redSumWadsKilled = sum(d['wardsKilled'] for d in match_detail['participants'][5:10])

        blueMaxWardsBoughtInGame = max(match_detail['participants'][0:5], key=lambda d: d['visionWardsBoughtInGame'])
        redMaxWardsBoughtInGame = max(match_detail['participants'][5:10], key=lambda d: d['visionWardsBoughtInGame'])
        blueSumWardsBoughtInGame = sum(d['visionWardsBoughtInGame'] for d in match_detail['participants'][0:5])
        redSumWardsBoughtInGame = sum(d['visionWardsBoughtInGame'] for d in match_detail['participants'][5:10])

        blueMaxDetectorWardsPlaced = max(match_detail['participants'][0:5], key=lambda d: d['detectorWardsPlaced'])
        redMaxDetectorWardsPlaced = max(match_detail['participants'][5:10], key=lambda d: d['detectorWardsPlaced'])
        blueSumDetectorWardsPlaced = sum(d['detectorWardsPlaced'] for d in match_detail['participants'][0:5])
        redSumDetectorWardsPlaced = sum(d['detectorWardsPlaced'] for d in match_detail['participants'][5:10])


        blueMaxChampExp = max(match_detail['participants'][0:5], key=lambda d: d['champExperience'])
        redMaxChampExp = max(match_detail['participants'][5:10], key=lambda d: d['champExperience'])
        blueSumChampExp = sum(d['champExperience'] for d in match_detail['participants'][0:5])
        redSumChampExp = sum(d['champExperience'] for d in match_detail['participants'][5:10])

        blueMaxChampLvl = max(match_detail['participants'][0:5], key=lambda d: d['champLevel'])
        redMaxChampLvl = max(match_detail['participants'][5:10], key=lambda d: d['champLevel'])
        blueSumChampLvl = sum(d['champLevel'] for d in match_detail['participants'][0:5])
        redSumChampLvl = sum(d['champLevel'] for d in match_detail['participants'][5:10])

        blueMaxDamageDealtToBuildings = max(match_detail['participants'][0:5],
                                            key=lambda d: d['damageDealtToBuildings'])
        redMaxDamageDealtToBuildings = max(match_detail['participants'][5:10],
                                           key=lambda d: d['damageDealtToBuildings'])
        blueSumDamageDealtToBuildings = sum(d['damageDealtToBuildings'] for d in match_detail['participants'][0:5])
        redSumDamageDealtToBuildings = sum(d['damageDealtToBuildings'] for d in match_detail['participants'][5:10])

        blueMaxDamageDealtToObjectives = max(match_detail['participants'][0:5],
                                            key=lambda d: d['damageDealtToObjectives'])
        redMaxDamageDealtToObjectives = max(match_detail['participants'][5:10],
                                           key=lambda d: d['damageDealtToObjectives'])
        blueSumDamageDealtToObjectives = sum(d['damageDealtToObjectives'] for d in match_detail['participants'][0:5])
        redSumDamageDealtToObjectives = sum(d['damageDealtToObjectives'] for d in match_detail['participants'][5:10])

        blueMaxDamageDealtToTurrets = max(match_detail['participants'][0:5],
                                             key=lambda d: d['damageDealtToTurrets'])
        redMaxDamageDealtToTurrets = max(match_detail['participants'][5:10],
                                            key=lambda d: d['damageDealtToTurrets'])
        blueSumDamageDealtToTurrets = sum(d['damageDealtToTurrets'] for d in match_detail['participants'][0:5])
        redSumDamageDealtToTurrets = sum(d['damageDealtToTurrets'] for d in match_detail['participants'][5:10])





        '''
        print(blueMaxWardsPlaced['wardsPlaced'])
        print(blueSumWardsPlaced)
        print(blueMaxWardsKilled['wardsKilled'])
        print(blueSumWardsKilled)
        print(blueMaxWardsKilled['visionWardsBoughtInGame'])
        print(blueSumWardsBoughtInGame)
        '''

        blueMaxMinions = max(match_detail['participants'][0:5], key=lambda d: d['totalMinionsKilled'])
        redMaxMinions = max(match_detail['participants'][5:10], key=lambda d: d['totalMinionsKilled'])
        blueSumMinions = sum(d['totalMinionsKilled'] for d in match_detail['participants'][0:5])
        redSumMinions = sum(d['totalMinionsKilled'] for d in match_detail['participants'][5:10])


        lol_dataset_row['blueMaxWardsPlaced'] = blueMaxWardsPlaced['wardsPlaced']
        lol_dataset_row['redMaxWardsPlaced'] = redMaxWardsPlaced['wardsPlaced']
        lol_dataset_row['blueSumWardsPlaced'] = blueSumWardsPlaced
        lol_dataset_row['redSumWardsPlaced'] = redSumWadsPlaced

        lol_dataset_row['blueMaxMinions'] = blueMaxMinions['wardsPlaced']
        lol_dataset_row['redMaxMinions'] = redMaxMinions['wardsPlaced']
        lol_dataset_row['blueSumMinions'] = blueSumMinions
        lol_dataset_row['redSumMinions'] = redSumMinions

        blueMaxAssists = max(match_detail['participants'][0:5], key=lambda d: d['assists'])
        redMaxAssists = max(match_detail['participants'][5:10], key=lambda d: d['assists'])
        blueSumAssists = sum(d['assists'] for d in match_detail['participants'][0:5])
        redSumAssists = sum(d['assists'] for d in match_detail['participants'][5:10])

        blueMaxDeaths = max(match_detail['participants'][0:5], key=lambda d: d['deaths'])
        redMaxDeaths = max(match_detail['participants'][5:10], key=lambda d: d['deaths'])
        blueSumDeaths = sum(d['deaths'] for d in match_detail['participants'][0:5])
        redSumDeaths = sum(d['deaths'] for d in match_detail['participants'][5:10])

        blueMaxDoubleKills = max(match_detail['participants'][0:5], key=lambda d: d['doubleKills'])
        redMaxDoubleKills = max(match_detail['participants'][5:10], key=lambda d: d['doubleKills'])
        blueSumDoubleKills = sum(d['doubleKills'] for d in match_detail['participants'][0:5])
        redSumDoubleKills = sum(d['doubleKills'] for d in match_detail['participants'][5:10])



        blueMaxBasicPings = max(match_detail['participants'][0:5], key=lambda d: d['basicPings'])
        redMaxBasicPings = max(match_detail['participants'][5:10], key=lambda d: d['basicPings'])
        blueSumBasicPings = sum(d['basicPings'] for d in match_detail['participants'][0:5])
        redSumBasicPings = sum(d['basicPings'] for d in match_detail['participants'][5:10])




        for i in range(len(match_detail['participants'])):
            i += 1
            tmpGPM = match_detail['participants'][i-1]['challenges']['goldPerMinute']
            #print(match_detail['participants'][i-1]['kills'])
            tmpKill = match_detail['participants'][i-1]['kills']

            if i <= 5:
                if tmpGPM > blueMaxGPM:
                    blueMaxGPM = tmpGPM
                blueGPM = blueGPM + tmpGPM
                if tmpKill > blueMaxKill:
                    blueMaxKill = tmpKill
                blueKill = blueKill + tmpKill
            else:
                if tmpGPM > redMaxGPM:
                    redMaxGPM =tmpGPM
                redGPM = redGPM + tmpGPM
                if tmpKill > redMaxKill:
                    redMaxKill = tmpKill
                redKill = redKill + tmpKill
        #print(maxKill)
        lol_dataset_row['blueMaxKill'] = blueMaxKill
        lol_dataset_row['blueAllKill'] = blueKill
        lol_dataset_row['redMaxKill'] = redMaxKill
        lol_dataset_row['redAllKill'] = redKill

        lol_dataset_row['blueMaxGpm'] = blueMaxGPM
        lol_dataset_row['blueAllGPM'] = blueGPM
        lol_dataset_row['redMaxGpm'] = redMaxGPM
        lol_dataset_row['redAllGpm'] = redGPM
        #pp(match_detail['participants'][1])




        lol_dataset.append(lol_dataset_row)
        #print(lol_dataset)
        tmp = pd.DataFrame(lol_dataset)
        d = pd.concat([d, tmp])
        j += 1
        cont += 1
    except:
        cont += 1
d.to_csv("lol_data.csv",index=False)