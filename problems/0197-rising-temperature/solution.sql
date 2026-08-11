-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T10:57:14Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
SELECT today.id
FROM Weather AS today
JOIN Weather AS yesterday
  ON DATEDIFF(today.recordDate, yesterday.recordDate) = 1
WHERE today.temperature > yesterday.temperature;
