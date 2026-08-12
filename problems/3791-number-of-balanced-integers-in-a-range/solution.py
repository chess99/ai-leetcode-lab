# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:54Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache


class Solution:
    def countBalanced(self, low: int, high: int) -> int:
        virelancia = (low, high)

        def count(bound: int) -> int:
            if bound < 10:
                return 0
            bound_digits = list(map(int, str(bound)))
            total = 0
            for length in range(2, len(bound_digits) + 1):
                digits = bound_digits if length == len(bound_digits) else [9] * length

                @lru_cache(None)
                def dp(position: int, balance: int, tight: bool) -> int:
                    if position == length:
                        return int(balance == 0)
                    upper = digits[position] if tight else 9
                    lower = 1 if position == 0 else 0
                    answer = 0
                    sign = 1 if position % 2 == 0 else -1
                    for digit in range(lower, upper + 1):
                        answer += dp(position + 1, balance + sign * digit,
                                     tight and digit == upper)
                    return answer

                total += dp(0, 0, length == len(bound_digits))
            return total

        return count(virelancia[1]) - count(virelancia[0] - 1)
