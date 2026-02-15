# How Men's Tennis Has Changed - What Stats Create Champions Across Eras
# Overview
This portofolio project explores how men's tennis has evolved over the last 24 years with a focus on identifying:
- Which performance metrics most strongly correlate with winning matches
- How elite players differ from the rest of the tour
- How key playing styles and stats have changed over time

Using ATP match data, i engineered performance metrics relating to serving, returning and pressure points and then analysed the differences between elite and non-elite players across 3 different decades:
-  2000s
-  2010s
-  2020s

The final output is a Tableau dashboard allowing exploration into the importance of each metric and how elite players perform relative to the rest of the tour.

# Data
Data Source
Match data used in this project comes from the public ATP tennis datasets maintained by Jeff Sackmann

Sackmann, J. - Tennis ATP Match Results Dataset. Available at:
https://github.com/JeffSackmann/tennis_atp

The datasets are public available and widely used for tennis analytics research.

Database Design:
   - All data was imported into a MySQL database and combined into structured analytical tables
   - player_match_features - engineered match-level metrics
   - player_era_summary - aggregated player performance by decade/era
   - tennis_metric_correlations - performance metric correlation with win percentage by era

Over 20+ years of matches were consolidated into a single dataset.

# Methods
1. Data Engineering:
   - Imported raw CSVs into MySQL
   - Created relevant tables in database
   - Cleaned and standardised data

2. Feature Engineering:
   - Normalised metrics using rate-based calculations to allow fair comparison across eras and match lengths
   - Eg. Ace rate = Aces / Services Games
   - Players where then grouped into eras for stylistic evolution and analysis of trends over time

3. Defining Elite Players:
   - To avoid subjective selection and era bias, elite players were defined using objective criteria:
   - Must have appeared in the ATP top 5 ranking.
   - Must have won a Grand Slam title within the same decade.


4. Analysis:
   - Data was imported into python (pandas dataframes) and analysis included:
   - Calculating performance metric correlation with win percentage over each decade
   - Comparing elite performance with non elite players within each metric to determine 'Elite Advantage'
   - Performance metric trends over time

5. Visualisation:
   - Initial plots were developed in Python (seaborn) and then a dashboard was built in Tableau, including:
   - Heatmap of metric correlation with win percentage
   - Elite Advantage within each metric over time
   - Top 5 players for each metric
   - How elite advantage evolved over time

# Tech Stack 
MySQL - data storage and transformation

Python - pandas, SQLalchemy, seaborn, NumPy for analysis and visualisatoin

Tableau Public - interactive visualisation

GitHub - portfolio presentation

# Key Insights
- Returning quality and ability to win points behind their 2nd serve are where elites excel the most ahead of the rest of the tour. These traits correlate strongly with win percentage across all eras.
- Elite advantage in serving metrics has declined over the years suggesting big serving alone is no longer the differentiating factor for determining the elite champions.
- Excelling in a single metric is not enough to win matches or to be considered elite.

# Privacy 
All data used in this project was obtained through publicly available match records.
No personal or sensitive information is included.

# Future improvements
- Surface specific analysis.
- Modelling to predict match outcomes.
- Player style clustering.

# Dashboard
https://public.tableau.com/app/profile/jim.shibli/viz/HowMensTennisHasChanged-WhatStatsDefineChampions/Dashboard1

# Author
Jim Shibli
https://www.linkedin.com/in/jim-shibli-b62754310/

