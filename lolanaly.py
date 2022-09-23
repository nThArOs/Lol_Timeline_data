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

df = pd.read_csv('lol_data.csv')

feature_list_blue = ['blueWin','blueKill','blueBaron','blueFirstBaron','blueDragon','blueFirstDragon','blueInhibitor','blueFirstInhibitor','blueTower','blueFirstTower','blueRiftHerald','blueFirstRiftHerald'
                ,'redWin','redKill','redBaron','redFirstBaron','redDragon','redFirstDragon','redInhibitor','redFirstInhibitor','redTower','redFirstTower','redRiftHerald','redFirstRiftHerald']
new_df = df[feature_list_blue]

corr = new_df.corr()
print('Positive Correlations:')
print(corr.loc['blueWin'].sort_values(ascending=False)[1:10])
print('\n')
print('Negative Correlations:')
print(corr.loc['blueWin'].sort_values(ascending=True)[1:10])

