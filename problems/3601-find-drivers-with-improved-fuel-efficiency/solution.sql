-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T22:15:56Z
-- Experiment: ai-leetcode-lab, round 1
WITH efficiency AS (
    SELECT driver_id,
           AVG(CASE WHEN MONTH(trip_date) <= 6 THEN distance_km / fuel_consumed END) AS first_avg,
           AVG(CASE WHEN MONTH(trip_date) >= 7 THEN distance_km / fuel_consumed END) AS second_avg
    FROM trips
    GROUP BY driver_id
)
SELECT d.driver_id, d.driver_name,
       ROUND(e.first_avg, 2) AS first_half_avg,
       ROUND(e.second_avg, 2) AS second_half_avg,
       ROUND(e.second_avg - e.first_avg, 2) AS efficiency_improvement
FROM drivers d JOIN efficiency e ON d.driver_id = e.driver_id
WHERE e.first_avg IS NOT NULL AND e.second_avg IS NOT NULL
  AND e.second_avg > e.first_avg
ORDER BY efficiency_improvement DESC, d.driver_name;
