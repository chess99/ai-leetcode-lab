-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T10:57:15Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
SELECT x, y, z,
       CASE WHEN x + y > z AND x + z > y AND y + z > x
            THEN 'Yes' ELSE 'No' END AS triangle
FROM Triangle;
