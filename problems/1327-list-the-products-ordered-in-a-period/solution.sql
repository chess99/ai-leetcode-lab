-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T11:53:16Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
SELECT p.product_name, SUM(o.unit) AS unit
FROM Products AS p
JOIN Orders AS o
  ON p.product_id = o.product_id
WHERE o.order_date >= '2020-02-01'
  AND o.order_date < '2020-03-01'
GROUP BY p.product_id, p.product_name
HAVING SUM(o.unit) >= 100;
