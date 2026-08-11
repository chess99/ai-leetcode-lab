# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:32:15Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def divide(self, a: int, b: int) -> int:
        if a == -(1 << 31) and b == -1:
            return (1 << 31) - 1
        negative = (a < 0) != (b < 0)
        dividend = -a if a < 0 else a
        divisor = -b if b < 0 else b
        quotient = 0
        while dividend >= divisor:
            value, multiple = divisor, 1
            while dividend >= value << 1:
                value <<= 1
                multiple <<= 1
            dividend -= value
            quotient += multiple
        return -quotient if negative else quotient
