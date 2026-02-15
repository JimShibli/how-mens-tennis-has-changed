-- Create Player/Career Summary Table
CREATE TABLE player_career_summary AS
SELECT
    player_id,
    player_name,
    

    COUNT(*) AS matches_played,
    ROUND((AVG(won_match)), 3) AS win_pct,

    ROUND(AVG(ace_rate), 3) AS avg_ace_rate,
    ROUND(AVG(df_rate), 3) AS avg_df_rate,
    ROUND(AVG(first_serve_pct), 3) AS avg_first_serve_pct,
    ROUND(AVG(first_serve_win_pct), 3) AS avg_first_serve_win_pct,
    ROUND(AVG(second_serve_win_pct), 3) AS avg_second_serve_win_pct,
    ROUND(AVG(service_games_won_pct), 3) AS avg_hold_rate,
    ROUND(AVG(return_games_won_pct), 3) AS avg_break_rate,
    ROUND(AVG(break_point_win_pct), 3) AS avg_bp_conversion

FROM player_match_features
GROUP BY player_id, player_name;
