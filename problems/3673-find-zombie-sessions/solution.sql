-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-12T17:28:46Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
SELECT session_id,
       user_id,
       TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp))
           AS session_duration_minutes,
       SUM(event_type = 'scroll') AS scroll_count
FROM app_events
GROUP BY session_id, user_id
HAVING TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp)) > 30
   AND SUM(event_type = 'scroll') >= 5
   AND SUM(event_type = 'click') < 0.2 * SUM(event_type = 'scroll')
   AND SUM(event_type = 'purchase') = 0
ORDER BY scroll_count DESC, session_id;
