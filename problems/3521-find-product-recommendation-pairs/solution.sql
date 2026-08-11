-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T22:15:53Z
-- Experiment: ai-leetcode-lab, round 1
SELECT p1.product_id AS product1_id,
       p2.product_id AS product2_id,
       i1.category AS product1_category,
       i2.category AS product2_category,
       COUNT(*) AS customer_count
FROM ProductPurchases p1
JOIN ProductPurchases p2
  ON p1.user_id = p2.user_id AND p1.product_id < p2.product_id
JOIN ProductInfo i1 ON i1.product_id = p1.product_id
JOIN ProductInfo i2 ON i2.product_id = p2.product_id
GROUP BY p1.product_id, p2.product_id, i1.category, i2.category
HAVING COUNT(*) >= 3
ORDER BY customer_count DESC, product1_id, product2_id;
