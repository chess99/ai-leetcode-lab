-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T10:21:41Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
SELECT e.name AS Employee
FROM Employee AS e
JOIN Employee AS m
  ON e.managerId = m.id
WHERE e.salary > m.salary;
