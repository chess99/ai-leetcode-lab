-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T12:23:26Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
SELECT r.contest_id,
       ROUND(100 * COUNT(*) / u.total, 2) AS percentage
FROM Register AS r
CROSS JOIN (SELECT COUNT(*) AS total FROM Users) AS u
GROUP BY r.contest_id, u.total
ORDER BY percentage DESC, contest_id;
