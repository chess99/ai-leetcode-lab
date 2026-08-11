-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T21:46:15Z
-- Experiment: ai-leetcode-lab, round 1
SELECT
    transaction_date,
    COALESCE(SUM(CASE WHEN amount % 2 = 1 THEN amount END), 0) AS odd_sum,
    COALESCE(SUM(CASE WHEN amount % 2 = 0 THEN amount END), 0) AS even_sum
FROM transactions
GROUP BY transaction_date
ORDER BY transaction_date;
