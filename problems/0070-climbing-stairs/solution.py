# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:13:53Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def climbStairs(self, n: int) -> int:
        previous, current = 1, 1
        for _ in range(n):
            previous, current = current, previous + current
        return previous
