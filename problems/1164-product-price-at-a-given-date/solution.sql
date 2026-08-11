-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T18:26:23Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
SELECT product_id, new_price AS price
FROM Products
WHERE (product_id, change_date) IN (
    SELECT product_id, MAX(change_date)
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
)
UNION
SELECT DISTINCT product_id, 10 AS price
FROM Products AS p
WHERE NOT EXISTS (
    SELECT 1
    FROM Products AS prior
    WHERE prior.product_id = p.product_id
      AND prior.change_date <= '2019-08-16'
);
