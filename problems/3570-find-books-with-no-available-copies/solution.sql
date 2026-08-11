-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T15:04:25Z
-- Experiment: ai-leetcode-lab, round 1
SELECT lb.book_id, lb.title, lb.author, lb.genre, lb.publication_year,
       COUNT(br.record_id) AS current_borrowers
FROM library_books AS lb
JOIN borrowing_records AS br
  ON br.book_id = lb.book_id AND br.return_date IS NULL
GROUP BY lb.book_id, lb.title, lb.author, lb.genre, lb.publication_year, lb.total_copies
HAVING COUNT(br.record_id) = lb.total_copies
ORDER BY current_borrowers DESC, lb.title ASC;
