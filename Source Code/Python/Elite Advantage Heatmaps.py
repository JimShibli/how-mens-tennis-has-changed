# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 14:24:23 2026

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

#tables into databases from query 
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

metric_labels = {'avg_ace_rate': 'Ace Rate',
                 'avg_df_rate': 'Double Fault Rate',
                 'avg_first_serve_pct': '1st Serve In %',
                 'avg_first_serve_win_pct': '1st Serve Win %',
                 'avg_second_serve_win_pct': '2nd Serve Win %',
                 'avg_hold_rate': 'Hold Rate',
                 'avg_break_rate': 'Break Rate',
                 'avg_bp_conversion': 'Break Point Conversion %'}


#Order eras and handle datatypes
era_order = ['2000s', '2010s', '2020s']
player_era_summary['era'] = pd.Categorical(player_era_summary['era'], categories=era_order, ordered=True)

#stats for elite players vs non elite split by era in pivot table
elite_v_tour_era_stats = player_era_summary.groupby(['era', 'elite'])[summary_metrics].mean()
elite_v_tour_era_pivot = elite_v_tour_era_stats.unstack('elite')

#calculate definite difference between elite and non 
elite_advantage_era = (elite_v_tour_era_pivot.xs(1, level='elite', axis=1)- elite_v_tour_era_pivot.xs(0, level='elite', axis=1))

#show difference in each era and sort by largest difference
for era in elite_advantage_era.index:
    print(f"\nElite advantage in {era}")
    print(elite_advantage_era.loc[era].sort_values(ascending=False))

#create plot ready version of elite advantage
elite_advantage_long = (
    elite_advantage_era
    .reset_index()
    .melt(id_vars='era', var_name='metric', value_name='elite_advantage'))

metrics_sorted = (elite_advantage_era.mean(axis=0).sort_values(ascending=False).index)

elite_advantage_plot = (elite_advantage_era[metrics_sorted].T)

plt.figure(figsize=(10, 6))
ax = sns.heatmap(elite_advantage_plot,
                 annot=True,
                 fmt=".2f",
                 cmap='Blues',
                 center=0)

# Replace y-axis labels on the plot
ax.set_yticklabels([metric_labels.get(label.get_text(), label.get_text())
                    for label in ax.get_yticklabels()],
                    rotation=0)
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)


plt.title("Elite Advantage of Performance Metrics By Era")
plt.tight_layout()
plt.grid()
plt.show()


