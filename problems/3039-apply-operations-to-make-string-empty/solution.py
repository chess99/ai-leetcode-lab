# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:36Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter


class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        counts = Counter(s)
        maximum = max(counts.values())
        last = {char: index for index, char in enumerate(s)}
        return ''.join(char for index, char in enumerate(s) if counts[char] == maximum and last[char] == index)
