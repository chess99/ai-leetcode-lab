-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T10:57:15Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
SELECT e.name, b.bonus
FROM Employee AS e
LEFT JOIN Bonus AS b ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;
