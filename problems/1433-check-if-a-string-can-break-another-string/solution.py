# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:49:32Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        first = sorted(s1)
        second = sorted(s2)
        return (all(a >= b for a, b in zip(first, second))
                or all(a <= b for a, b in zip(first, second)))
