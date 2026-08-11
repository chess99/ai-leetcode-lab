# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:07:31Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        value = abs(x)
        reversed_value = 0
        while value:
            value, digit = divmod(value, 10)
            reversed_value = reversed_value * 10 + digit
        result = sign * reversed_value
        if result < -(2**31) or result > 2**31 - 1:
            return 0
        return result
