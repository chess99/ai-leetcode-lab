-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T18:28:40Z
-- Experiment: ai-leetcode-lab, round 1
SELECT person_name
FROM Queue
WHERE turn = (
    SELECT MAX(q.turn)
    FROM Queue AS q
    WHERE (SELECT SUM(weight) FROM Queue WHERE turn <= q.turn) <= 1000
);
