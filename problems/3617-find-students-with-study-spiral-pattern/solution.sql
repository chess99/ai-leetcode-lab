-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-sol
-- Reasoning effort: medium
-- Profile: sol-medium
-- Experiment: ai-leetcode-lab, replacement candidate after Terra runtime error
# Write your MySQL query statement below
WITH ordered_sessions AS (
    SELECT ss.*,
           ROW_NUMBER() OVER (
               PARTITION BY ss.student_id
               ORDER BY ss.session_date, ss.session_id
           ) AS rn,
           LAG(ss.session_date) OVER (
               PARTITION BY ss.student_id
               ORDER BY ss.session_date, ss.session_id
           ) AS previous_date
    FROM study_sessions AS ss
),
student_summary AS (
    SELECT student_id,
           COUNT(*) AS session_count,
           COUNT(DISTINCT subject) AS cycle_length,
           SUM(hours_studied) AS total_study_hours,
           MAX(
               CASE
                   WHEN previous_date IS NOT NULL
                        AND DATEDIFF(session_date, previous_date) > 2
                   THEN 1
                   ELSE 0
               END
           ) AS has_date_gap
    FROM ordered_sessions
    GROUP BY student_id
),
slot_summary AS (
    SELECT os.student_id,
           MOD(os.rn - 1, ss.cycle_length) AS cycle_slot,
           COUNT(DISTINCT os.subject) AS subjects_in_slot
    FROM ordered_sessions AS os
    INNER JOIN student_summary AS ss
        ON ss.student_id = os.student_id
    WHERE ss.cycle_length >= 3
      AND ss.session_count >= 2 * ss.cycle_length
      AND ss.has_date_gap = 0
    GROUP BY os.student_id,
             MOD(os.rn - 1, ss.cycle_length)
),
qualified_students AS (
    SELECT ss.student_id,
           ss.cycle_length,
           ss.total_study_hours
    FROM student_summary AS ss
    INNER JOIN slot_summary AS sl
        ON sl.student_id = ss.student_id
    WHERE ss.cycle_length >= 3
      AND ss.session_count >= 2 * ss.cycle_length
      AND ss.has_date_gap = 0
    GROUP BY ss.student_id,
             ss.cycle_length,
             ss.total_study_hours
    HAVING COUNT(*) = ss.cycle_length
       AND MAX(sl.subjects_in_slot) = 1
)
SELECT s.student_id,
       s.student_name,
       s.major,
       qs.cycle_length,
       qs.total_study_hours
FROM qualified_students AS qs
INNER JOIN students AS s
    ON s.student_id = qs.student_id
ORDER BY qs.cycle_length DESC,
         qs.total_study_hours DESC;
