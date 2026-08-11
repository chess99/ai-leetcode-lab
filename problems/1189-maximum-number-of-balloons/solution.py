# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:41:49Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        return min(counts['b'], counts['a'], counts['l'] // 2,
                   counts['o'] // 2, counts['n'])
