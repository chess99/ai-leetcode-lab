# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:40:22Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def fib(self, n: int) -> int:
        previous, current = 0, 1
        for _ in range(n):
            previous, current = current, (previous + current) % 1_000_000_007
        return previous
