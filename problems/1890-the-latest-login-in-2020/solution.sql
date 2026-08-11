-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T12:51:27Z
-- Experiment: ai-leetcode-lab, round 1
SELECT user_id, MAX(time_stamp) AS last_stamp
FROM Logins
WHERE time_stamp >= '2020-01-01' AND time_stamp < '2021-01-01'
GROUP BY user_id;
