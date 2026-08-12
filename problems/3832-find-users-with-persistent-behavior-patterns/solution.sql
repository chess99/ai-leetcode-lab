-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-12T17:28:56Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
WITH daily AS (
    SELECT user_id, action_date, MAX(action) AS action
    FROM activity
    GROUP BY user_id, action_date
    HAVING COUNT(*) = 1
), numbered AS (
    SELECT user_id, action_date, action,
           DATE_SUB(action_date, INTERVAL
               ROW_NUMBER() OVER (
                   PARTITION BY user_id, action ORDER BY action_date
               ) DAY) AS island
    FROM daily
), streaks AS (
    SELECT user_id, action, COUNT(*) AS streak_length,
           MIN(action_date) AS start_date,
           MAX(action_date) AS end_date
    FROM numbered
    GROUP BY user_id, action, island
), ranked AS (
    SELECT streaks.*,
           ROW_NUMBER() OVER (
               PARTITION BY user_id
               ORDER BY streak_length DESC, start_date, action
           ) AS choice
    FROM streaks
    WHERE streak_length >= 5
)
SELECT user_id, action, streak_length, start_date, end_date
FROM ranked
WHERE choice = 1
ORDER BY streak_length DESC, user_id;
