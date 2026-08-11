-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T11:43:13Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
SELECT query_name,
       ROUND(AVG(rating / position), 2) AS quality,
       ROUND(100 * AVG(rating < 3), 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;
