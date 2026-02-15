-- Grand Slam Champions
CREATE TABLE grand_slam_champions AS
SELECT winner_id,
		winner_name,
        COUNT(winner_name) AS num_grand_slams
FROM raw_matches
WHERE tourney_level = 'G'
AND round = 'F'
GROUP BY winner_id, winner_name;

SELECT *
FROM grand_slam_champions