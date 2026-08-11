# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:27Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        total = a + b + c
        largest_pile = max(a, b, c)
        return min(total // 2, total - largest_pile)
