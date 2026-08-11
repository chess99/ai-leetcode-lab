-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T18:26:24Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
SELECT ROUND(
    100 * AVG(order_date = customer_pref_delivery_date),
    2
) AS immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (
    SELECT customer_id, MIN(order_date)
    FROM Delivery
    GROUP BY customer_id
);
