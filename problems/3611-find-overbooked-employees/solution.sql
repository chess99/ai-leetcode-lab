-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T22:15:56Z
-- Experiment: ai-leetcode-lab, round 1
WITH weekly AS (
    SELECT employee_id,
           YEARWEEK(meeting_date, 1) AS week_id,
           SUM(duration_hours) AS meeting_hours
    FROM meetings
    GROUP BY employee_id, YEARWEEK(meeting_date, 1)
), heavy AS (
    SELECT employee_id, COUNT(*) AS meeting_heavy_weeks
    FROM weekly
    WHERE meeting_hours > 20
    GROUP BY employee_id
)
SELECT e.employee_id, e.employee_name, e.department, h.meeting_heavy_weeks
FROM employees e JOIN heavy h ON e.employee_id = h.employee_id
WHERE h.meeting_heavy_weeks >= 2
ORDER BY h.meeting_heavy_weeks DESC, e.employee_name;
