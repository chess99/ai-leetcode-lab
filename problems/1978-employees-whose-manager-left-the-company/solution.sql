-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T12:52:50Z
-- Experiment: ai-leetcode-lab, round 1
SELECT employee_id FROM Employees
WHERE salary < 30000 AND manager_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id;
