# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 10:29:38 2026

@author: Jim
"""

import pandas as pd
from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt

engine = create_engine("mysql+pymysql://root:Chicago22!@localhost:3306/atp_data")
tables = pd.read_sql("SHOW TABLES", engine)

#query for player_match_features
query_pmf = """
SELECT *
FROM player_match_features
"""

#tables into databases from query 
player_match_features = pd.read_sql(query_pmf, engine)

match_metrics = ['ace_rate',
                 'df_rate',
                 'first_serve_pct',
                 'serve_points_won_pct',
                 'first_serve_win_pct',
                 'second_serve_win_pct',
                 'service_games_won_pct',
                 'return_games_won_pct',
                 'break_points_generated_pct',
                 'break_point_save_pct',
                 'break_point_win_pct']

winner_means = player_match_features[(player_match_features['won_match'] == 1)][match_metrics].mean()
loser_means  = player_match_features[(player_match_features['won_match'] == 0)][match_metrics].mean()


winner_loser_comparison = pd.DataFrame({'winners': winner_means,
                                        'losers': loser_means,
                                        'diff': winner_means - loser_means}
                                         ).sort_values('diff', ascending=False)

print(winner_loser_comparison)

#This is slightly less relevant as it just compares winners to losers with little regard to elite vs non, and suffers circular reasoning. 
#Of course winners do better in all stats and have correlation with games won etc
#Need to do comparison of Elite advantage for whole eras.