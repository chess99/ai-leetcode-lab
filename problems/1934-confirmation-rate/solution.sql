-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T19:48:06Z
-- Experiment: ai-leetcode-lab, round 1
SELECT s.user_id, ROUND(AVG(c.action = 'confirmed'), 2) AS confirmation_rate
FROM Signups AS s LEFT JOIN Confirmations AS c ON s.user_id = c.user_id
GROUP BY s.user_id;
