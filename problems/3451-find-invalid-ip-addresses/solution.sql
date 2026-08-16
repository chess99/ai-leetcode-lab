-- AI solution attribution
-- Original creator: Codex Desktop / gpt-5.6-terra / medium / terra-medium
-- Terra handoff: full-IPv4 validation incorrectly rejected empty segments
-- Current client: Codex Desktop
-- Current model: gpt-5.6-sol
-- Current reasoning effort: medium
-- Current profile: sol-medium
SELECT ip, COUNT(*) AS invalid_count
FROM logs
WHERE LENGTH(ip) - LENGTH(REPLACE(ip, '.', '')) <> 3
   OR REGEXP_LIKE(
        ip,
        '(^|\\.)(0[0-9]+|25[6-9]|2[6-9][0-9]|[3-9][0-9]{2}|[0-9]{4,})(\\.|$)'
      )
GROUP BY ip
ORDER BY invalid_count DESC, ip DESC;
