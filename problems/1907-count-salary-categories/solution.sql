-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T19:48:03Z
-- Experiment: ai-leetcode-lab, round 1
SELECT 'Low Salary' AS category, COUNT(*) AS accounts_count
FROM Accounts
WHERE income < 20000
UNION ALL
SELECT 'Average Salary' AS category, COUNT(*) AS accounts_count
FROM Accounts
WHERE income BETWEEN 20000 AND 50000
UNION ALL
SELECT 'High Salary' AS category, COUNT(*) AS accounts_count
FROM Accounts
WHERE income > 50000;
