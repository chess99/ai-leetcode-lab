-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T18:41:14Z
-- Experiment: ai-leetcode-lab, round 1
(SELECT u.name AS results
 FROM MovieRating AS r JOIN Users AS u ON r.user_id = u.user_id
 GROUP BY r.user_id, u.name
 ORDER BY COUNT(*) DESC, u.name
 LIMIT 1)
UNION ALL
(SELECT m.title AS results
 FROM MovieRating AS r JOIN Movies AS m ON r.movie_id = m.movie_id
 WHERE r.created_at >= '2020-02-01' AND r.created_at < '2020-03-01'
 GROUP BY r.movie_id, m.title
 ORDER BY AVG(r.rating) DESC, m.title
 LIMIT 1);
