# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:52:41Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def integerReplacement(self, n: int) -> int:
        steps = 0
        while n != 1:
            if n % 2 == 0: n //= 2
            elif n == 3 or n % 4 == 1: n -= 1
            else: n += 1
            steps += 1
        return steps
