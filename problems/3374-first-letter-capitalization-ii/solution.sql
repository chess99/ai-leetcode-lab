-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-12T15:59:05Z
-- Experiment: ai-leetcode-lab, round 1
WITH RECURSIVE chars AS (
    SELECT content_id, content_text, 1 AS pos, '' AS converted_text
    FROM user_content
    UNION ALL
    SELECT content_id, content_text, pos + 1,
           CONCAT(converted_text,
             CASE WHEN pos = 1 OR SUBSTRING(content_text, pos - 1, 1) IN (' ', '-')
                  THEN UPPER(SUBSTRING(content_text, pos, 1))
                  ELSE LOWER(SUBSTRING(content_text, pos, 1)) END)
    FROM chars
    WHERE pos <= CHAR_LENGTH(content_text)
)
SELECT content_id, content_text AS original_text, converted_text
FROM chars
WHERE pos = CHAR_LENGTH(content_text) + 1
ORDER BY content_id;
