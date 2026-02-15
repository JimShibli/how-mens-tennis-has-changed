# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 14:55:03 2026

@author: Jim
"""

import pandas as pd
from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt

engine = create_engine("mysql+pymysql://root:Chicago22!@localhost:3306/atp_data")
tables = pd.read_sql("SHOW TABLES", engine)

plt.style.use('C:/Users/Jim/OneDrive/Documents/Homework/Uni/pubstyle.mplstyle.txt')

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


#create plot ready version of elite_v_tour
elite_v_tour_era_stats_long = (
    elite_v_tour_era_stats
    .reset_index()
    .melt(id_vars=['era','elite'], value_vars=summary_metrics, var_name='metric', value_name='average'))

elite_v_tour_era_stats_long['player_group'] = elite_v_tour_era_stats_long['elite'].map({1:'Elite', 0:'Non-Elite'})

avg_across_era = (elite_v_tour_era_stats_long.groupby(['metric', 'player_group'])['average'].mean().reset_index())

metric_order = (
    avg_across_era
    .pivot(index='metric', columns='player_group', values='average')
    .assign(diff=lambda x: x['Elite'] - x['Non-Elite'])
    .sort_values('diff', ascending=False)
    .index
)

plt.figure(figsize=(10, 6))

ax = sns.barplot(
    data=avg_across_era,
    x='metric',
    y='average',
    hue='player_group',
    order=metric_order,
    hue_order=['Non-Elite', 'Elite'],
    palette={'Non-Elite': 'tab:blue', 'Elite': 'tab:orange'}
)

# Fix x-axis labels (plot only)
ax.set_xticklabels(
    [metric_labels.get(m, m) for m in metric_order],
    rotation=30,
    ha='right'
)

plt.title("Elite vs Non-Elite Performance Metrics (All Eras)")
plt.xlabel("")
plt.ylabel("Average Value")
plt.legend(title="")
plt.tight_layout()
plt.show()

for era in era_order:
    
    era_df = elite_v_tour_era_stats_long[
        elite_v_tour_era_stats_long['era'] == era
    ]

    plt.figure(figsize=(9, 5))

    ax = sns.barplot(
        data=era_df,
        x='metric',
        y='average',
        hue='player_group',
        order=metric_order
    )

    # Fix x-axis labels (plot only)
    ax.set_xticklabels(
        [metric_labels.get(m, m) for m in metric_order],
        rotation=30,
        ha='right'
    )

    plt.title(f"Elite vs Non-Elite Performance Metrics ({era})")
    plt.xlabel("")
    plt.ylabel("Average Value")
    plt.legend(title="")
    plt.tight_layout()
    plt.show()

elite_v_tour_era_stats_long.to_csv('elite_v_tour_era_stats.csv', index=False)