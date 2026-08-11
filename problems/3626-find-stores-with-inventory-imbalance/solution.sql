-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T22:15:56Z
-- Experiment: ai-leetcode-lab, round 1
WITH ranked AS (
    SELECT i.*,
           ROW_NUMBER() OVER (PARTITION BY store_id ORDER BY price DESC, quantity DESC) AS expensive_rank,
           ROW_NUMBER() OVER (PARTITION BY store_id ORDER BY price, quantity DESC) AS cheap_rank,
           COUNT(*) OVER (PARTITION BY store_id) AS product_count
    FROM inventory i
), chosen AS (
    SELECT store_id,
           MAX(CASE WHEN expensive_rank = 1 THEN product_name END) AS most_exp_product,
           MAX(CASE WHEN expensive_rank = 1 THEN quantity END) AS expensive_quantity,
           MAX(CASE WHEN cheap_rank = 1 THEN product_name END) AS cheapest_product,
           MAX(CASE WHEN cheap_rank = 1 THEN quantity END) AS cheap_quantity,
           MAX(product_count) AS product_count
    FROM ranked
    GROUP BY store_id
)
SELECT s.store_id, s.store_name, s.location, c.most_exp_product, c.cheapest_product,
       ROUND(c.cheap_quantity / c.expensive_quantity, 2) AS imbalance_ratio
FROM stores s JOIN chosen c ON s.store_id = c.store_id
WHERE c.product_count >= 3 AND c.expensive_quantity < c.cheap_quantity
ORDER BY imbalance_ratio DESC, s.store_name;
