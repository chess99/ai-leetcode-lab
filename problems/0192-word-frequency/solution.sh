# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:30:59Z
# Experiment: ai-leetcode-lab, round 1
# Read from the file words.txt and output the word frequency list to stdout.
tr -s '[:space:]' '\n' < words.txt | sed '/^$/d' | sort | uniq -c | sort -k1,1nr -k2,2 | awk '{print $2, $1}'
