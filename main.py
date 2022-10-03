#LOAD LIB
from riotwatcher import LolWatcher, ApiError
import os
from numpy import mean
import pandas as pd

def get_match_history(summonerName, player_region):
    match_history = lol_watcher.match.matchlist_by_puuid(region = player_region,
                                                         puuid = summonerName['puuid'])
    return match_history

def get_challenger_leadboar(queue_type, player_region):
    #GET THE DATA OF THE API TO A DATAFRAME
    chall_player = pd.DataFrame.from_dict(lol_watcher.league.challenger_by_queue(region = player_region,
                                                                                 queue = queue_type)['entries'])
    #Organise leadbord by LeaguePoint
    chall_player = chall_player[
        ['leaguePoints', 'rank', 'summonerName', 'wins', 'losses', 'hotStreak', 'veteran', 'freshBlood', 'inactive',
         'summonerId']]
    chall_player = chall_player.sort_values(by="leaguePoints", ascending = False)
    #Reset index to match the previous sorting
    chall_player.reset_index(drop=True, inplace=True)
    summoner_names = chall_player['summonerName'].tolist()
    return chall_player, summoner_names

def get_summoner_puuid(summonerName, player_region):
    summpuuid = []
    for i in range(len(summonerName)):
        try:
            summoner = lol_watcher.summoner.by_name(player_region, summonerName[i])
            summpuuid.append(
                {
                "summonerNameee":summoner['name'],
                "puuid":summoner['puuid']
                }
            )
        except:
            print(summonerName[i])
    return summpuuid

def update_leadboard_with_puuid(summonerPUUID,leadboard):
    #print(summonerPUUID)
    #print(leadboard)
    leadboard["puuid"] = summonerPUUID['puuid']
    print(leadboard)
    #leadboard.to_csv("leadboarduuid.csv", index=False)
    #leadBoardpuuid.to_csv("leadboarduuid.csv", index=False)
    return

def update_leadboard(newleadboard):
    oldleadboard = pd.read_csv('leadboarduuid.csv')
    old_list = oldleadboard['summonerName'].tolist()
    new_list = newleadboard['summonerName'].tolist()
    old = set(old_list)
    new = set(new_list)
    missing = list(sorted(old - new))
    added = list(sorted(new - old))
    print(old)
    print(new)
    print('missing:', missing)
    print('added:', added)


def get_matchlist(leadboard, my_region):
    listMatchId = []
    for index,row in leadboard.iterrows():
        try:
            matchlist = lol_watcher.match.matchlist_by_puuid(my_region, row['puuid'])
            print(matchlist)
            listMatchId.append(matchlist)

        except:
            print("fail pour")
    print(listMatchId)
    df = pd.DataFrame(listMatchId)
    mat = df.values.tolist()
    flat_list_match = flatten(mat)
    list_match = list(set(flat_list_match))
    # df.to_csv("matchlist.csv", index=False)
    # matchlist = pd.read_csv("matchlist.csv")
    return list_match

def flatten(l):
    return [item for sublist in l for item in sublist]




def match_info(my_region, matchId):
    match_info = lol_watcher.match.by_id(my_region, matchId)
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

    match_metadata = pd.DataFrame.from_dict([lol_dataset_row])
    player_list = pd.DataFrame(match_detail['participants'])
    player_list = player_list.sort_values(by=['individualPosition'],ascending=False)

    #PRINT OPTION
    pd.set_option('display.max_columns', None)  # or 1000
    pd.set_option('display.max_rows', None)  # or 1000
    pd.set_option('display.max_colwidth', None)  # or 199
    #print(player_list)

    #DROP LES COLUMNS RELOU
    player_list.drop('challenges', inplace =True, axis=1)
    player_list.drop('perks', inplace=True, axis=1)

    #separate player
    blueTeam = player_list[player_list['teamId'] == 100]
    topBlue = blueTeam[blueTeam['teamPosition']=="TOP"]
    junglerBlue = blueTeam[blueTeam['teamPosition']=="JUNGLE"]
    midBlue= blueTeam[blueTeam['teamPosition']=="MIDDLE"]
    adcBlue= blueTeam[blueTeam['teamPosition']=="BOTTOM"]
    supportBlue= blueTeam[blueTeam['teamPosition']=="UTILITY"]
    redTeam = player_list[player_list['teamId'] == 200]
    topRed = redTeam[redTeam['teamPosition'] == "TOP"]
    junglerRed = redTeam[redTeam['teamPosition'] == "JUNGLE"]
    midRed = redTeam[redTeam['teamPosition'] == "MIDDLE"]
    adcRed = redTeam[redTeam['teamPosition'] == "BOTTOM"]
    supportRed = redTeam[redTeam['teamPosition'] == "UTILITY"]


    team = [topRed,junglerRed,midRed,adcRed,supportRed,topBlue,junglerBlue,midBlue,adcBlue,supportBlue]
    teamConcat = pd.concat(team)

    default_value = matchId
    teamConcat.insert(2,'gameId',default_value)

    team_multi = teamConcat.set_index(['gameId','teamId','teamPosition'])
    team_multi.to_csv("math_detail_test.csv",index=False)
    df = pd.read_csv("math_detail_test.csv")
    print(team_multi)
    print(df)





    return

#-----------------------------MAIN-------------------------------------#
lol_watcher = LolWatcher('RGAPI-34f7bc11-170d-4423-a20e-9f3f878c62b6')
my_region = 'euw1'
queue_type = "RANKED_SOLO_5x5"
#print(get_challenger_leadboar(queue_type, my_region))
#leadBoard, listName = get_challenger_leadboar(queue_type, my_region)
#Summppuuid = pd.DataFrame.from_dict(get_summoner_puuid(listName,my_region))
#update_leadboard(leadBoard)
#leadBoardop = pd.read_csv("leadboarduuid.csv")
#match_list = get_matchlist(leadBoardop, my_region)

matchlist = pd.read_csv("matchlist.csv")
mat = matchlist.values.tolist()
flat_list_match = flatten(mat)
list_match = list(set(flat_list_match))
#matchId = "EUW1_6084347239"
print(list_match[2])

matchId = list_match[2]
gametest = match_info(my_region, matchId)
#print(gametest)






