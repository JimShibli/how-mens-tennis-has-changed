-- Put all matches into one single table for all years
-- Add year column for each one

CREATE TABLE raw_matches AS
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2000
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2001
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2002
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2003
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2004
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2005
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2006
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2007
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2008
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2009
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2010
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2011
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2012
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2013
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2014
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2015
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2016
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2017
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2018
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2019
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2020
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2021
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2022
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2023
UNION ALL
SELECT *, YEAR(tourney_date) AS year
FROM atp_matches_2024;
