-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-sol
-- Reasoning effort: medium
-- Profile: sol-medium
-- Experiment: ai-leetcode-lab, TLE follow-up candidate
WITH histories AS (
    SELECT employee_id,
           LEFT(
               GROUP_CONCAT(
                   rating
                   ORDER BY review_date DESC, review_id DESC
                   SEPARATOR ''
               ),
               3
           ) AS recent_ratings
    FROM performance_reviews
    GROUP BY employee_id
), recent_reviews AS (
    SELECT employee_id,
           CAST(SUBSTRING(recent_ratings, 1, 1) AS UNSIGNED) AS latest_rating,
           CAST(SUBSTRING(recent_ratings, 2, 1) AS UNSIGNED) AS middle_rating,
           CAST(SUBSTRING(recent_ratings, 3, 1) AS UNSIGNED) AS earliest_rating
    FROM histories
    WHERE CHAR_LENGTH(recent_ratings) = 3
)
SELECT e.employee_id,
       e.name,
       r.latest_rating - r.earliest_rating AS improvement_score
FROM recent_reviews AS r
JOIN employees AS e
  ON e.employee_id = r.employee_id
WHERE r.earliest_rating < r.middle_rating
  AND r.middle_rating < r.latest_rating
ORDER BY improvement_score DESC, e.name ASC;
