-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T17:16:54Z
-- Experiment: ai-leetcode-lab, round 1
SELECT ROUND(
    COUNT(next_day.player_id) / COUNT(DISTINCT first_login.player_id),
    2
) AS fraction
FROM (
    SELECT player_id, MIN(event_date) AS first_date
    FROM Activity
    GROUP BY player_id
) AS first_login
LEFT JOIN Activity AS next_day
    ON next_day.player_id = first_login.player_id
    AND next_day.event_date = DATE_ADD(first_login.first_date, INTERVAL 1 DAY);
