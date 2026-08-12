-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-12T16:39:44Z
-- Experiment: ai-leetcode-lab, round 1
WITH RECURSIVE
hierarchy AS (
    SELECT employee_id, 1 AS lvl
    FROM Employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT employee.employee_id, hierarchy.lvl + 1
    FROM Employees AS employee
    JOIN hierarchy ON employee.manager_id = hierarchy.employee_id
),
team AS (
    SELECT employee_id AS manager_id, employee_id AS member_id
    FROM Employees
    UNION ALL
    SELECT team.manager_id, employee.employee_id
    FROM team
    JOIN Employees AS employee ON employee.manager_id = team.member_id
)
SELECT
    employee.employee_id,
    employee.employee_name,
    hierarchy.lvl AS level,
    COUNT(*) - 1 AS team_size,
    SUM(member.salary) AS budget
FROM Employees AS employee
JOIN hierarchy ON hierarchy.employee_id = employee.employee_id
JOIN team ON team.manager_id = employee.employee_id
JOIN Employees AS member ON member.employee_id = team.member_id
GROUP BY employee.employee_id, employee.employee_name, hierarchy.lvl
ORDER BY level ASC, budget DESC, employee.employee_name ASC;
