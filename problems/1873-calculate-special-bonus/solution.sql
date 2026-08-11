-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T12:51:36Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
SELECT employee_id, CASE WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' THEN salary ELSE 0 END AS bonus
FROM Employees
ORDER BY employee_id;
