-- AI solution attribution
-- Client: Codex Desktop
-- Model: gpt-5.6-terra
-- Reasoning effort: medium
-- Profile: terra-medium
-- Created: 2026-08-11T21:59:19Z
-- Experiment: ai-leetcode-lab, round 1
SELECT sample_id, dna_sequence, species,
       (dna_sequence LIKE 'ATG%') AS has_start,
       (dna_sequence REGEXP '(TAA|TAG|TGA)$') AS has_stop,
       (dna_sequence LIKE '%ATAT%') AS has_atat,
       (dna_sequence LIKE '%GGG%') AS has_ggg
FROM Samples
ORDER BY sample_id;
