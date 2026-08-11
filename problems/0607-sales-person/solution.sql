-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T10:57:15Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT o.sales_id
    FROM Orders AS o
    JOIN Company AS c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
);
