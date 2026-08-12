-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-12T02:47:44Z
-- Experiment: ai-leetcode-lab, round 1
SELECT customer_id
FROM customer_transactions
GROUP BY customer_id
HAVING SUM(transaction_type = 'purchase') >= 3
   AND DATEDIFF(MAX(transaction_date), MIN(transaction_date)) >= 30
   AND SUM(transaction_type = 'refund') / COUNT(*) < 0.2
ORDER BY customer_id;
