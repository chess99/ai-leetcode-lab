-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-12T17:28:52Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
WITH top_students AS (
    SELECT user_id
    FROM course_completions
    GROUP BY user_id
    HAVING COUNT(*) >= 5 AND AVG(course_rating) >= 4
), ordered_courses AS (
    SELECT
        c.user_id,
        c.course_name AS second_course,
        LAG(c.course_name) OVER (
            PARTITION BY c.user_id
            ORDER BY c.completion_date, c.course_id
        ) AS first_course
    FROM course_completions AS c
    INNER JOIN top_students AS t USING (user_id)
)
SELECT first_course, second_course, COUNT(*) AS transition_count
FROM ordered_courses
WHERE first_course IS NOT NULL
GROUP BY first_course, second_course
ORDER BY transition_count DESC, first_course, second_course;
