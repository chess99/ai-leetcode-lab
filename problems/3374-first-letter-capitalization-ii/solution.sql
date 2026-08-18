-- Original creator: Codex Desktop / gpt-5.6-terra / medium / terra-medium
-- sol-medium failure handed off to sol-high
-- Client: Codex Desktop
-- Model: gpt-5.6-sol
-- Reasoning effort: high
-- Profile: sol-high
-- Experiment: ai-leetcode-lab, round 1
WITH RECURSIVE converted AS (
    SELECT
        content_id,
        content_text,
        1 AS pos,
        LOWER(content_text) AS converted_text,
        REGEXP_LIKE(
            SUBSTRING_INDEX(content_text, ' ', 1),
            '^[A-Za-z]+-[A-Za-z]+$',
            'c'
        ) AS is_simple_hyphenated_word
    FROM user_content

    UNION ALL

    SELECT
        content_id,
        content_text,
        pos + 1,
        CASE
            WHEN pos = 1
              OR SUBSTRING(content_text, pos - 1, 1) = ' '
              OR (
                  is_simple_hyphenated_word
                  AND SUBSTRING(content_text, pos - 1, 1) = '-'
              )
            THEN INSERT(
                converted_text,
                pos,
                1,
                UPPER(SUBSTRING(converted_text, pos, 1))
            )
            ELSE converted_text
        END AS converted_text,
        CASE
            WHEN SUBSTRING(content_text, pos, 1) = ' '
            THEN REGEXP_LIKE(
                SUBSTRING_INDEX(SUBSTRING(content_text, pos + 1), ' ', 1),
                '^[A-Za-z]+-[A-Za-z]+$',
                'c'
            )
            ELSE is_simple_hyphenated_word
        END AS is_simple_hyphenated_word
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
