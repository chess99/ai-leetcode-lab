-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T18:26:22Z
-- Experiment: ai-leetcode-lab, round 1
SELECT u.user_id AS buyer_id,
       u.join_date,
       COUNT(o.order_id) AS orders_in_2019
FROM Users AS u
LEFT JOIN Orders AS o
  ON o.buyer_id = u.user_id
 AND o.order_date >= '2019-01-01'
 AND o.order_date < '2020-01-01'
GROUP BY u.user_id, u.join_date;
