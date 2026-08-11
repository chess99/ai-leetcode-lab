-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T12:24:46Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
SELECT start_activity.machine_id,
       ROUND(AVG(end_activity.timestamp - start_activity.timestamp), 3) AS processing_time
FROM Activity AS start_activity
JOIN Activity AS end_activity
  ON start_activity.machine_id = end_activity.machine_id
 AND start_activity.process_id = end_activity.process_id
WHERE start_activity.activity_type = 'start'
  AND end_activity.activity_type = 'end'
GROUP BY start_activity.machine_id;
