# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:59:13Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def waysToStep(self, n: int) -> int:
        mod = 1_000_000_007
        first, second, third = 1, 1, 2
        if n == 1:
            return second
        if n == 2:
            return third
        for _ in range(3, n + 1):
            first, second, third = second, third, (first + second + third) % mod
        return third
