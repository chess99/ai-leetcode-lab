-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T12:56:28Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
SELECT e.employee_id
FROM Employees AS e LEFT JOIN Salaries AS s ON e.employee_id = s.employee_id
WHERE s.employee_id IS NULL
UNION
SELECT s.employee_id
FROM Salaries AS s LEFT JOIN Employees AS e ON e.employee_id = s.employee_id
WHERE e.employee_id IS NULL
ORDER BY employee_id;
