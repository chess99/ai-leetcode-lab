# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:30:59Z
# Experiment: ai-leetcode-lab, round 1
# Read from the file file.txt and print its transposed content to stdout.
awk '{for (i = 1; i <= NF; i++) columns[i] = columns[i] (NR == 1 ? "" : " ") $i} END {for (i = 1; i <= NF; i++) print columns[i]}' file.txt
