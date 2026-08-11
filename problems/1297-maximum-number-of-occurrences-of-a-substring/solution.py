# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:37:16Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        occurrences = Counter()
        for start in range(len(s) - minSize + 1):
            substring = s[start:start + minSize]
            if len(set(substring)) <= maxLetters:
                occurrences[substring] += 1
        return max(occurrences.values(), default=0)
