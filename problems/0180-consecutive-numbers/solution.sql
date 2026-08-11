-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T16:30:19Z
-- Experiment: ai-leetcode-lab, round 1
SELECT DISTINCT first_log.num AS ConsecutiveNums
FROM Logs AS first_log
JOIN Logs AS second_log
    ON second_log.id = first_log.id + 1
    AND second_log.num = first_log.num
JOIN Logs AS third_log
    ON third_log.id = first_log.id + 2
    AND third_log.num = first_log.num;
