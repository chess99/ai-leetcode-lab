# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:29:00Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache


class Solution:
    def countFancy(self, l: int, r: int) -> int:
        morvaxelin = (l, r)

        def good(value: int) -> bool:
            digits = list(map(int, str(value)))
            return (len(digits) == 1
                    or all(a < b for a, b in zip(digits, digits[1:]))
                    or all(a > b for a, b in zip(digits, digits[1:])))

        def count(bound: int) -> int:
            if bound <= 0:
                return 0
            digits = tuple(map(int, str(bound)))

            @lru_cache(None)
            def dp(position: int, digit_sum: int, previous: int,
                   increasing: bool, decreasing: bool,
                   started: bool, tight: bool) -> int:
                if position == len(digits):
                    if not started:
                        return 0
                    return int((increasing or decreasing) or good(digit_sum))
                upper = digits[position] if tight else 9
                total = 0
                for digit in range(upper + 1):
                    next_tight = tight and digit == upper
                    if not started and digit == 0:
                        total += dp(position + 1, 0, 10, True, True,
                                    False, next_tight)
                    elif not started:
                        total += dp(position + 1, digit, digit, True, True,
                                    True, next_tight)
                    else:
                        total += dp(position + 1, digit_sum + digit, digit,
                                    increasing and previous < digit,
                                    decreasing and previous > digit,
                                    True, next_tight)
                return total

            return dp(0, 0, 10, True, True, False, True)

        return count(morvaxelin[1]) - count(morvaxelin[0] - 1)
