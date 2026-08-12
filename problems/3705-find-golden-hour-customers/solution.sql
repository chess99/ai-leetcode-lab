-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-12T02:47:48Z
-- Experiment: ai-leetcode-lab, round 1
WITH customer_stats AS (
    SELECT customer_id,
           COUNT(*) AS total_orders,
           SUM(CASE
                   WHEN TIME(order_timestamp) BETWEEN '11:00:00' AND '14:00:00'
                     OR TIME(order_timestamp) BETWEEN '18:00:00' AND '21:00:00'
                   THEN 1 ELSE 0
               END) AS peak_orders,
           COUNT(order_rating) AS rated_orders,
           AVG(order_rating) AS raw_average_rating
    FROM restaurant_orders
    GROUP BY customer_id
)
SELECT customer_id,
       total_orders,
       ROUND(100.0 * peak_orders / total_orders, 2) AS peak_hour_percentage,
       ROUND(raw_average_rating, 2) AS average_rating
FROM customer_stats
WHERE total_orders >= 3
  AND peak_orders * 100 >= total_orders * 60
  AND raw_average_rating >= 4.00
  AND rated_orders * 2 >= total_orders
ORDER BY average_rating DESC, customer_id DESC;
