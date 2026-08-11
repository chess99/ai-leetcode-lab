-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T10:22:25Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
SELECT c.name AS Customers
FROM Customers AS c
WHERE NOT EXISTS (
  SELECT 1
  FROM Orders AS o
  WHERE o.customerId = c.id
);
