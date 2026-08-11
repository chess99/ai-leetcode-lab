# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:11Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def addMinimum(self, word: str) -> int:
        groups = 1 + sum(a >= b for a, b in zip(word, word[1:]))
        return groups * 3 - len(word)
