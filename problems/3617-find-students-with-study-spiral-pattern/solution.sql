-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-12T16:38:46Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
WITH ordered AS (
    SELECT ss.*,
           LAG(session_date) OVER (PARTITION BY student_id ORDER BY session_date, session_id) AS prev_date,
           ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY session_date, session_id) AS rn
    FROM study_sessions AS ss
),
valid AS (
    SELECT *,
           CASE WHEN prev_date IS NULL OR DATEDIFF(session_date, prev_date) <= 2 THEN 0 ELSE 1 END AS new_group
    FROM ordered
),
groups AS (
    SELECT *, SUM(new_group) OVER (PARTITION BY student_id ORDER BY rn) AS grp
    FROM valid
),
sequenced AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY student_id, grp ORDER BY rn) AS pos
    FROM groups
),
candidates AS (
    SELECT student_id, grp, COUNT(*) AS cnt,
           COUNT(DISTINCT subject) AS cycle_length,
           SUM(hours_studied) AS total_study_hours
    FROM sequenced
    GROUP BY student_id, grp
),
positions AS (
    SELECT q.student_id, q.grp, MOD(q.pos - 1, c.cycle_length) AS slot,
           COUNT(DISTINCT q.subject) AS subject_count
    FROM sequenced AS q
    JOIN candidates AS c ON c.student_id = q.student_id AND c.grp = q.grp
    GROUP BY q.student_id, q.grp, MOD(q.pos - 1, c.cycle_length)
),
patterns AS (
    SELECT c.*
    FROM candidates AS c
    JOIN positions AS p ON p.student_id = c.student_id AND p.grp = c.grp
    WHERE c.cnt >= 2 * c.cycle_length AND c.cycle_length >= 3
    GROUP BY c.student_id, c.grp, c.cnt, c.cycle_length, c.total_study_hours
    HAVING COUNT(*) = c.cycle_length AND MAX(p.subject_count) = 1
)
SELECT s.student_id, s.student_name, s.major,
       p.cycle_length, p.total_study_hours
FROM patterns AS p
JOIN students AS s ON s.student_id = p.student_id
ORDER BY p.cycle_length DESC, p.total_study_hours DESC;
