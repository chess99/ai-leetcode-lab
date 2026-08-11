-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T11:27:35Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
SELECT p.project_id, ROUND(AVG(e.experience_years), 2) AS average_years
FROM Project AS p
JOIN Employee AS e ON p.employee_id = e.employee_id
GROUP BY p.project_id;
