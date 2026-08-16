-- AI solution attribution (terra-medium failure handed off to sol-medium)
-- Client: Codex Desktop
-- Model: gpt-5.6-sol
-- Reasoning effort: medium
-- Profile: sol-medium
-- Experiment: ai-leetcode-lab, round 1
WITH RECURSIVE converted AS (
    SELECT
        content_id,
        content_text,
        1 AS pos,
        LOWER(content_text) AS converted_text
    FROM user_content

    UNION ALL

    SELECT
        content_id,
        content_text,
        pos + 1,
        CASE
            WHEN pos = 1
              OR SUBSTRING(content_text, pos - 1, 1) IN (' ', '-')
            THEN INSERT(
                converted_text,
                pos,
                1,
                UPPER(SUBSTRING(converted_text, pos, 1))
            )
            ELSE converted_text
        END AS converted_text
    FROM converted
    WHERE pos <= CHAR_LENGTH(content_text)
)
SELECT
    content_id,
    content_text AS original_text,
    converted_text
FROM converted
WHERE pos = COALESCE(CHAR_LENGTH(content_text), 0) + 1
ORDER BY content_id;
