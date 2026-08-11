# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:05:11Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        from collections import Counter
        a, b = Counter(word1), Counter(word2)
        return all(abs(a[ch] - b[ch]) <= 3 for ch in a.keys() | b.keys())
