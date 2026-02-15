-- Tour averages for feature stats
SELECT 
	era,
    AVG(win_pct),
    AVG(avg_ace_rate),
    AVG(avg_df_rate),
    AVG(avg_first_serve_pct),
    AVG(avg_first_serve_win_pct),
    AVG(avg_second_serve_win_pct),
    AVG(avg_hold_rate),
    AVG(avg_break_rate),
    AVG(avg_bp_conversion)
FROM player_era_summary
GROUP BY era;

-- Non-elite feature averages 
SELECT 
	era,
    AVG(win_pct),
    AVG(avg_ace_rate),
    AVG(avg_df_rate),
    AVG(avg_first_serve_pct),
    AVG(avg_first_serve_win_pct),
    AVG(avg_second_serve_win_pct),
    AVG(avg_hold_rate),
    AVG(avg_break_rate),
    AVG(avg_bp_conversion)
FROM player_era_summary
WHERE elite = 0
GROUP BY era;

-- Elite feature averages 
SELECT 
	era,
    AVG(win_pct),
    AVG(avg_ace_rate),
    AVG(avg_df_rate),
    AVG(avg_first_serve_pct),
    AVG(avg_first_serve_win_pct),
    AVG(avg_second_serve_win_pct),
    AVG(avg_hold_rate),
    AVG(avg_break_rate),
    AVG(avg_bp_conversion)
FROM player_era_summary
WHERE elite = 1
GROUP BY era;

-- Compare averages for feature stats between elite and not
SELECT 
	era,
    elite,
    AVG(win_pct),
    AVG(avg_ace_rate),
    AVG(avg_df_rate),
    AVG(avg_first_serve_pct),
    AVG(avg_first_serve_win_pct),
    AVG(avg_second_serve_win_pct),
    AVG(avg_hold_rate),
    AVG(avg_break_rate),
    AVG(avg_bp_conversion)
FROM player_era_summary
GROUP BY era, elite;
    
		