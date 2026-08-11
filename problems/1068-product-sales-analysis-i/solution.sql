-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T11:27:35Z
-- Experiment: ai-leetcode-lab, round 1
# Write your MySQL query statement below
SELECT p.product_name, s.year, s.price
FROM Sales AS s
JOIN Product AS p ON s.product_id = p.product_id;
