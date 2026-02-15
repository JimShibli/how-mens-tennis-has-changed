CREATE VIEW player_matches_features_view AS
SELECT player_id,
		player_name,
        opponent_id,
        opponent_name,
        won_match,
        score,
        year AS match_year,
        tourney_name,
        surface,
        era,
        
		-- Serve quality 
        -- Ace rate
        CASE WHEN service_games > 0
			THEN ROUND((aces / service_games), 3)
            END AS ace_rate,
            
		-- Double fault rate
		CASE WHEN service_games > 0
			THEN ROUND((df / service_games), 3)
            END AS df_rate,
            
		-- First serve %
        CASE WHEN serve_points > 0
			THEN ROUND((first_serves_in / serve_points), 3)
            END AS first_serve_pct,
            
		-- Serve points won %
        CASE WHEN serve_points > 0
			THEN ROUND(((first_serve_points_won + second_serve_points_won) / serve_points), 3)
            END AS serve_points_won_pct,
		
        -- First serve point won %
		CASE WHEN first_serves_in > 0
			THEN ROUND((first_serve_points_won / first_serves_in), 3)
            END AS first_serve_win_pct,
		
        -- Second serve points won %
        CASE WHEN serve_points - first_serves_in > 0
			THEN ROUND((second_serve_points_won / (serve_points - first_serves_in)), 3)
            END AS second_serve_win_pct,
            
		-- Hold rate
        CASE WHEN service_games > 0
			THEN ROUND(((service_games - (break_points_faced - break_points_saved)) / service_games), 3)
            END AS service_games_won_pct,
            
		-- Returning quality
		-- Break rate
        CASE WHEN return_games > 0
			THEN ROUND((break_points_won / return_games), 3)
            END AS return_games_won_pct,
            
		-- Break point generation rate
        CASE WHEN return_games > 0
			THEN ROUND((break_points_generated / return_games) , 3)
            END AS break_points_generated_pct,
            
		-- Clutch metrics
        -- Break point win %
        CASE WHEN break_points_generated > 0 
			THEN ROUND((break_points_won / break_points_generated), 3)
            END AS break_point_win_pct,
            
		-- Break point save %
        CASE WHEN break_points_faced > 0
			THEN ROUND((break_points_saved / break_points_faced), 3)
            END AS break_point_save_pct
            
FROM player_matches;
           
        
        