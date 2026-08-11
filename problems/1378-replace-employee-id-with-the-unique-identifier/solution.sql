-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T11:53:04Z
-- Experiment: ai-leetcode-lab, round 1
SELECT u.unique_id, e.name
FROM Employees e LEFT JOIN EmployeeUNI u ON e.id=u.id;
