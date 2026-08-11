# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:27:18Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minSteps(self, n: int) -> int:
        steps = 0
        factor = 2
        while factor * factor <= n:
            while n % factor == 0:
                steps += factor
                n //= factor
            factor += 1
        return steps + n if n > 1 else steps
