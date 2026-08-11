-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T22:15:55Z
-- Experiment: ai-leetcode-lab, round 1
WITH ranked AS (
    SELECT employee_id, review_date, rating,
           ROW_NUMBER() OVER (PARTITION BY employee_id ORDER BY review_date DESC) AS rn
    FROM performance_reviews
), recent AS (
    SELECT employee_id,
           MAX(CASE WHEN rn = 1 THEN rating END) AS latest,
           MAX(CASE WHEN rn = 2 THEN rating END) AS middle,
           MAX(CASE WHEN rn = 3 THEN rating END) AS earliest
    FROM ranked
    WHERE rn <= 3
    GROUP BY employee_id
)
SELECT e.employee_id, e.name, r.latest - r.earliest AS improvement_score
FROM recent r JOIN employees e ON e.employee_id = r.employee_id
WHERE r.earliest IS NOT NULL AND r.earliest < r.middle AND r.middle < r.latest
ORDER BY improvement_score DESC, e.name;
