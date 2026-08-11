# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:36Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        frequencies = sorted(Counter(word).values(), reverse=True)
        return sum(frequency * (index // 8 + 1) for index, frequency in enumerate(frequencies))
