# -*- coding: utf-8 -*-
"""
Created on Mon Feb  9 15:14:32 2026

@author: Jim
"""

import pandas as pd
from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt

engine = create_engine("mysql+pymysql://root:Chicago22!@localhost:3306/atp_data")
tables = pd.read_sql("SHOW TABLES", engine)


#query for player_era_summary
query_pes = """
SELECT *
FROM player_era_summary
WHERE matches_played > 5
"""

#tables into dataframes from query
player_era_summary = pd.read_sql(query_pes, engine)

#list containing metrics
summary_metrics = ['avg_ace_rate', 
                   'avg_df_rate', 
                   'avg_first_serve_pct',
                   'avg_first_serve_win_pct', 
                   'avg_second_serve_win_pct', 
                   'avg_hold_rate',
                   'avg_break_rate', 
                   'avg_bp_conversion']

summary_metrics_reduced = ['avg_first_serve_pct',
                           'avg_first_serve_win_pct', 
                           'avg_second_serve_win_pct', 
                           'avg_hold_rate',
                           'avg_break_rate']

#Order eras and handle datatypes
player_era_summary['elite'] = player_era_summary['elite'].astype(float)
player_era_summary['avg_ace_rate'] = player_era_summary['avg_ace_rate'].astype(float)
era_order = ['2000s', '2010s', '2020s']
player_era_summary['era'] = pd.Categorical(player_era_summary['era'], categories=era_order, ordered=True)


#average of each metric by era, then compared between elite players and non
era_stats = (player_era_summary.groupby(['era'])[summary_metrics].mean().unstack())
elite_v_tour_stats = player_era_summary.groupby(['elite'])[summary_metrics].mean()


#stats for elite players vs non elite split by era in pivot table
elite_v_tour_era_stats = player_era_summary.groupby(['era', 'elite'])[summary_metrics].mean()
elite_v_tour_era_pivot = elite_v_tour_era_stats.unstack('elite')

#calculate definite difference between elite and non 
elite_advantage_era = (elite_v_tour_era_pivot.xs(1, level='elite', axis=1) - elite_v_tour_era_pivot.xs(0, level='elite', axis=1))

#show difference in each era and sort by largest difference
for era in elite_advantage_era.index:
    print(f"\nElite advantage in {era}")
    print(
        elite_advantage_era
        .loc[era]
        .sort_values(ascending=False))
    
#create plot ready version of elite advantage
elite_advantage_long = (elite_advantage_era.reset_index().melt(id_vars='era', var_name='metric', value_name='elite_advantage'))

#metrics we are going to test for correlation with win ratio in each ear
corr_metrics = ['avg_ace_rate', 
                'avg_df_rate', 
                'avg_first_serve_pct',
                'avg_first_serve_win_pct', 
                'avg_second_serve_win_pct', 
                'avg_hold_rate',
                'avg_break_rate', 
                'avg_bp_conversion']

metric_labels = {'avg_ace_rate': 'Ace Rate',
                 'avg_df_rate': 'Double Fault Rate',
                 'avg_first_serve_pct': '1st Serve In %',
                 'avg_first_serve_win_pct': '1st Serve Win %',
                 'avg_second_serve_win_pct': '2nd Serve Win %',
                 'avg_hold_rate': 'Hold Rate',
                 'avg_break_rate': 'Break Rate',
                 'avg_bp_conversion': 'Break Point Conversion %'}


#create empty dict for correlation
corr_results = {}

#calculate correlation with win% for each metric
for era in player_era_summary['era'].unique():
    era_df = player_era_summary[player_era_summary['era'] == era]
    
    corr_results[era] = (era_df[corr_metrics].corrwith(era_df['win_pct']).sort_values(ascending=False))

for era, series in corr_results.items():
    print(f"\nCorrelation with win% in {era}")
    print(series)

#create df for correlation results
correlation_df = pd.DataFrame(corr_results)

#create plot ready version
corr_long = (
    correlation_df
    .reset_index()
    .melt(
        id_vars='index',
        var_name='era',
        value_name='corr_with_win_pct'
    )
    .rename(columns={'index': 'metric'})
)

corr_long['metric_label'] = corr_long['metric'].map(metric_labels)

plt.figure(figsize=(10, 6))
ax = sns.heatmap(correlation_df.drop(columns='mean_corr', errors='ignore'),
                 annot=True,
                 fmt=".2f",
                 cmap='Blues',
                 center=0)

# Replace y-axis labels ONLY on the plot
ax.set_yticklabels([metric_labels.get(label.get_text(), label.get_text())
                    for label in ax.get_yticklabels()],
                    rotation=0)

plt.title("Correlation of Performance Metrics with Win Percentage by Era")
plt.tight_layout()
plt.grid()
plt.show()

corr_long.to_csv("tennis_metric_correlations.csv", index=False)
