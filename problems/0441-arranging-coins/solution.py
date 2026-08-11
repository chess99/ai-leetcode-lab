# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:37:30Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def arrangeCoins(self, n: int) -> int:
        from math import isqrt
        return (isqrt(8 * n + 1) - 1) // 2
