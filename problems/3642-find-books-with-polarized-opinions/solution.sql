-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-12T02:47:42Z
-- Experiment: ai-leetcode-lab, round 1
SELECT b.book_id,
       b.title,
       b.author,
       b.genre,
       b.pages,
       MAX(r.session_rating) - MIN(r.session_rating) AS rating_spread,
       ROUND(SUM(r.session_rating <= 2 OR r.session_rating >= 4) / COUNT(*), 2) AS polarization_score
FROM books b
JOIN reading_sessions r ON r.book_id = b.book_id
GROUP BY b.book_id, b.title, b.author, b.genre, b.pages
HAVING COUNT(*) >= 5
   AND MAX(r.session_rating) >= 4
   AND MIN(r.session_rating) <= 2
   AND SUM(r.session_rating <= 2 OR r.session_rating >= 4) / COUNT(*) >= 0.6
ORDER BY polarization_score DESC, b.title DESC;
