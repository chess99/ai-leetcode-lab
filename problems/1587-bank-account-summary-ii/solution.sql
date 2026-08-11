-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T12:06:17Z
-- Experiment: ai-leetcode-lab, round 1
SELECT u.name, SUM(t.amount) AS balance
FROM Users u JOIN Transactions t ON u.account=t.account
GROUP BY u.account, u.name
HAVING balance > 10000;
