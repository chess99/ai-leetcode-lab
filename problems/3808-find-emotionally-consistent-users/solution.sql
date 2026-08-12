-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-12T03:13:35Z
-- Experiment: ai-leetcode-lab, round 1
WITH reaction_counts AS (
    SELECT user_id, reaction, COUNT(*) AS reaction_count,
           SUM(COUNT(*)) OVER (PARTITION BY user_id) AS total_count,
           ROW_NUMBER() OVER (
               PARTITION BY user_id
               ORDER BY COUNT(*) DESC, reaction
           ) AS reaction_rank
    FROM reactions
    GROUP BY user_id, reaction
)
SELECT user_id,
       reaction AS dominant_reaction,
       ROUND(reaction_count / total_count, 2) AS reaction_ratio
FROM reaction_counts
WHERE reaction_rank = 1
  AND total_count >= 5
  AND reaction_count * 10 >= total_count * 6
ORDER BY reaction_ratio DESC, user_id;
