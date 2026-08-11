-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T10:23:05Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
DELETE p1
FROM Person AS p1
JOIN Person AS p2
  ON p1.email = p2.email
 AND p1.id > p2.id;
