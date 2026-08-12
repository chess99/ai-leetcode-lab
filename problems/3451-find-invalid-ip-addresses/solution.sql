-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-12T16:39:41Z
-- Experiment: ai-leetcode-lab, round 1
SELECT ip, COUNT(*) AS invalid_count
FROM logs
WHERE NOT REGEXP_LIKE(
    ip,
    '^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?|0)(\\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?|0)){3}$'
)
GROUP BY ip
ORDER BY invalid_count DESC, ip DESC;
