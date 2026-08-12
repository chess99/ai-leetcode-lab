-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-12T05:38:44Z
-- Experiment: ai-leetcode-lab, round 1
SELECT t.request_at AS Day,
       ROUND(SUM(t.status != 'completed') / COUNT(*), 2) AS 'Cancellation Rate'
FROM Trips t
JOIN Users c ON c.users_id = t.client_id AND c.banned = 'No'
JOIN Users d ON d.users_id = t.driver_id AND d.banned = 'No'
WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at;
