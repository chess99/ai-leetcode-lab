-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T12:10:19Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
SELECT *
FROM Users
WHERE mail REGEXP BINARY '^[A-Za-z][A-Za-z0-9_.-]*@leetcode[.]com$';
