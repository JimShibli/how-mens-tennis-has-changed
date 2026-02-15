-- Grand Slam Champions By Era
CREATE VIEW grand_slam_champions_by_era AS
SELECT winner_id AS player_id,
		winner_name AS player_name,
        COUNT(winner_name) AS num_grand_slams,
        CASE
			WHEN year BETWEEN 2000 AND 2009 THEN '2000s'
			WHEN year BETWEEN 2010 AND 2019 THEN '2010s'
			ELSE '2020s'
    END AS era
FROM raw_matches
WHERE tourney_level = 'G'
AND round = 'F'
GROUP BY winner_id, winner_name, era;

SELECT *
FROM grand_slam_champions_by_era
ORDER BY num_grand_slams DESC;

-- Peak Ranking in Top 5
CREATE VIEW peak_ranking_within_era AS
SELECT player_id,
		player_name,
        era,
        MIN(ranking) AS peak_rank_in_era
FROM player_matches
GROUP BY player_id, player_name, era
HAVING MIN(ranking) <= 5;

SELECT *
FROM peak_ranking_within_era;

-- Combine criteria for elite players, peaked in top 5 and won a slam in the same era.
CREATE TABLE elite_players_by_era AS
SELECT r.player_id,
		r.player_name,
        r.era,
        r.peak_rank_in_era,
        s.num_grand_slams,
        1 AS elite
FROM peak_ranking_within_era AS r
JOIN grand_slam_champions_by_era AS s
ON r.player_id = s.player_id
AND r.era = s.era;

SELECT *
FROM elite_players_by_era;

-- Add column indicating elite status to main player era summaries
ALTER TABLE player_era_summary
ADD COLUMN elite TINYINT DEFAULT 0;

UPDATE player_era_summary AS p
JOIN elite_players_by_era AS e
	ON p.player_id = e.player_id
    AND p.era = e.era
SET p.elite = 1;

SELECT * 
FROM player_era_summary
WHERE elite = 1;
		


