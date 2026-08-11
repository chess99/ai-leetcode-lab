-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T10:57:15Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
SELECT *
FROM cinema
WHERE id % 2 = 1 AND description <> 'boring'
ORDER BY rating DESC;
