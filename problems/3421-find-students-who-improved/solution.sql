-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T21:59:18Z
-- Experiment: ai-leetcode-lab, round 1
WITH ranked AS (
    SELECT student_id, subject, score,
           ROW_NUMBER() OVER (PARTITION BY student_id, subject ORDER BY exam_date) AS first_rank,
           ROW_NUMBER() OVER (PARTITION BY student_id, subject ORDER BY exam_date DESC) AS last_rank
    FROM Scores
), summary AS (
    SELECT student_id, subject,
           MAX(CASE WHEN first_rank = 1 THEN score END) AS first_score,
           MAX(CASE WHEN last_rank = 1 THEN score END) AS latest_score,
           COUNT(*) AS exam_count
    FROM ranked
    GROUP BY student_id, subject
)
SELECT student_id, subject, first_score, latest_score
FROM summary
WHERE exam_count >= 2 AND latest_score > first_score
ORDER BY student_id, subject;
