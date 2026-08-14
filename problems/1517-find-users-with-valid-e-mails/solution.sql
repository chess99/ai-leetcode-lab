-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-sol
-- Reasoning effort: medium
-- Profile: sol-medium
-- Created: 2026-08-14
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
SELECT *
FROM Users
WHERE REGEXP_LIKE(
    mail,
    '^[A-Za-z][A-Za-z0-9_.-]*@leetcode[.]com$',
    'c'
);
