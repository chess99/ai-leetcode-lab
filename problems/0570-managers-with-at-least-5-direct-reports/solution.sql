-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T17:24:40Z
-- Experiment: ai-leetcode-lab, round 1
SELECT manager.name
FROM Employee AS manager
JOIN Employee AS report
    ON report.managerId = manager.id
GROUP BY manager.id, manager.name
HAVING COUNT(report.id) >= 5;
