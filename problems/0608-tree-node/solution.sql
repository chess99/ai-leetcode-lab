-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T17:24:42Z
-- Experiment: ai-leetcode-lab, round 1
SELECT parent.id,
       CASE
           WHEN parent.p_id IS NULL THEN 'Root'
           WHEN COUNT(child.id) = 0 THEN 'Leaf'
           ELSE 'Inner'
       END AS type
FROM Tree AS parent
LEFT JOIN Tree AS child
    ON parent.id = child.p_id
GROUP BY parent.id, parent.p_id;
