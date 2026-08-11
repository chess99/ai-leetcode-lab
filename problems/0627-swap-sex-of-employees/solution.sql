-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T10:57:16Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
UPDATE Salary
SET sex = CASE sex WHEN 'm' THEN 'f' ELSE 'm' END;
