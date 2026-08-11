# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:29:28Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for factor in (2, 3, 5):
            while n % factor == 0:
                n //= factor
        return n == 1
