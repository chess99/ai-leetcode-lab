# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:27:15Z
# Experiment: ai-leetcode-lab, round 1
from math import isqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = isqrt(c)
        while left <= right:
            total = left * left + right * right
            if total == c:
                return True
            if total < c:
                left += 1
            else:
                right -= 1
        return False
