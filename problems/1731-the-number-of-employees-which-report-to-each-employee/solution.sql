-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T12:31:10Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
SELECT manager.employee_id,
       manager.name,
       COUNT(report.employee_id) AS reports_count,
       ROUND(AVG(report.age)) AS average_age
FROM Employees AS manager
JOIN Employees AS report
  ON report.reports_to = manager.employee_id
GROUP BY manager.employee_id, manager.name
ORDER BY manager.employee_id;
