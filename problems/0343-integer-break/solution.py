# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:47:59Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3: return n - 1
        product = 1
        while n > 4: product *= 3; n -= 3
        return product * n
