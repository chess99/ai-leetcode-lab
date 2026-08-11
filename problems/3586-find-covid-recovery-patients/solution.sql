-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T22:15:55Z
-- Experiment: ai-leetcode-lab, round 1
WITH first_positive AS (
    SELECT patient_id, MIN(test_date) AS positive_date
    FROM covid_tests
    WHERE result = 'Positive'
    GROUP BY patient_id
), recovered AS (
    SELECT fp.patient_id, fp.positive_date, MIN(t.test_date) AS negative_date
    FROM first_positive fp
    JOIN covid_tests t ON t.patient_id = fp.patient_id
                     AND t.result = 'Negative'
                     AND t.test_date > fp.positive_date
    GROUP BY fp.patient_id, fp.positive_date
)
SELECT p.patient_id, p.patient_name, p.age,
       DATEDIFF(r.negative_date, r.positive_date) AS recovery_time
FROM recovered r JOIN patients p ON p.patient_id = r.patient_id
ORDER BY recovery_time, patient_name;
