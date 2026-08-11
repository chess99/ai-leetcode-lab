# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:42:24Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def fib(self, n: int) -> int:
        previous, current = 0, 1
        for _ in range(n):
            previous, current = current, previous + current
        return previous
