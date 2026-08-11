-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T15:16:00Z
-- Experiment: ai-leetcode-lab, round 1
WITH user_stats AS (
    SELECT user_id,
           COUNT(*) AS prompt_count,
           ROUND(AVG(tokens), 2) AS avg_tokens,
           MAX(tokens) AS max_tokens
    FROM prompts
    GROUP BY user_id
)
SELECT user_id, prompt_count, avg_tokens
FROM user_stats
WHERE prompt_count >= 3 AND max_tokens > avg_tokens
ORDER BY avg_tokens DESC, user_id ASC;
