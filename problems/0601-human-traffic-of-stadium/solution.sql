-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-12T06:02:56Z
-- Experiment: ai-leetcode-lab, round 1
SELECT DISTINCT a.* FROM Stadium a
JOIN Stadium b ON b.id BETWEEN a.id - 2 AND a.id + 2 AND b.people >= 100
JOIN Stadium c ON c.id BETWEEN a.id - 2 AND a.id + 2 AND c.people >= 100
WHERE a.people >= 100 AND ((a.id=b.id-1 AND b.id=c.id-1) OR (a.id=b.id+1 AND b.id=c.id+1) OR (b.id=a.id-1 AND a.id=c.id-1))
ORDER BY a.visit_date;
