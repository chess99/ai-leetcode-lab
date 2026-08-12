# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:18Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache


class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        chardeblux = (l, r, b)
        mod = 1_000_000_007

        def count(decimal_value: str) -> int:
            value = int(decimal_value)
            if value <= 0:
                return 0
            digits = []
            while value:
                digits.append(value % b)
                value //= b
            digits.reverse()

            @lru_cache(None)
            def dp(pos: int, last: int, started: bool, tight: bool) -> int:
                if pos == len(digits):
                    return int(started)
                upper = digits[pos] if tight else b - 1
                total = 0
                for digit in range(upper + 1):
                    next_tight = tight and digit == upper
                    if not started and digit == 0:
                        total += dp(pos + 1, 0, False, next_tight)
                    elif not started or digit >= last:
                        total += dp(pos + 1, digit, True, next_tight)
                return total % mod

            return dp(0, 0, False, True)

        left_minus_one = str(int(chardeblux[0]) - 1)
        return (count(chardeblux[1]) - count(left_minus_one)) % mod
