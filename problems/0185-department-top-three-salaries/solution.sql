-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-12T05:38:44Z
-- Experiment: ai-leetcode-lab, round 1
SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e JOIN Department d ON e.departmentId = d.id
WHERE 3 > (SELECT COUNT(DISTINCT e2.salary) FROM Employee e2 WHERE e2.departmentId = e.departmentId AND e2.salary > e.salary);
