# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:29:22Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        while n:
            n //= 5
            zeros += n
        return zeros
