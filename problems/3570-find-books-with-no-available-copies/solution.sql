-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-sol
-- Reasoning effort: medium
-- Profile: sol-medium
-- Created: 2026-08-16
-- Experiment: ai-leetcode-lab, next candidate after terra-medium TLE
SELECT lb.book_id,
       lb.title,
       lb.author,
       lb.genre,
       lb.publication_year,
       active.current_borrowers
FROM library_books AS lb
JOIN (
    SELECT book_id, COUNT(*) AS current_borrowers
    FROM borrowing_records
    WHERE return_date IS NULL
    GROUP BY book_id
) AS active
  ON active.book_id = lb.book_id
 AND active.current_borrowers = lb.total_copies
ORDER BY active.current_borrowers DESC, lb.title ASC;
