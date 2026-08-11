# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:10:37Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            multiple, value = 1, divisor
            while dividend >= (value << 1):
                value <<= 1
                multiple <<= 1
            dividend -= value
            quotient += multiple
        if negative:
            quotient = -quotient
        return min(max(quotient, -2**31), 2**31 - 1)
