-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T18:39:57Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
WITH daily AS (
    SELECT visited_on, SUM(amount) AS daily_amount
    FROM Customer
    GROUP BY visited_on
), rolling AS (
    SELECT visited_on,
           SUM(daily_amount) OVER (
               ORDER BY visited_on
               ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
           ) AS amount,
           COUNT(*) OVER (
               ORDER BY visited_on
               ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
           ) AS day_count
    FROM daily
)
SELECT visited_on, amount, ROUND(amount / 7, 2) AS average_amount
FROM rolling
WHERE day_count = 7
ORDER BY visited_on;
