# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:37Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        mavlorenti = (n, s, m)
        peaks = n // 2
        return s + peaks * m - max(0, peaks - 1)
