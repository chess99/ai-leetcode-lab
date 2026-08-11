-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T16:30:59Z
-- Experiment: ai-leetcode-lab, round 1
SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee AS e
JOIN Department AS d ON d.id = e.departmentId
WHERE e.salary = (
    SELECT MAX(other.salary)
    FROM Employee AS other
    WHERE other.departmentId = e.departmentId
);
