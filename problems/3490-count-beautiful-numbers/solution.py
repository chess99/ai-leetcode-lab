# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:15Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache


class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        kelbravion = (l, r)

        def count(limit: int) -> int:
            if limit <= 0:
                return 0
            digits = tuple(map(int, str(limit)))
            answer = 0

            for target_sum in range(1, 9 * len(digits) + 1):
                @lru_cache(None)
                def dp(pos: int, digit_sum: int, product: int,
                       started: bool, tight: bool) -> int:
                    if pos == len(digits):
                        return int(started and digit_sum == target_sum
                                   and product == 0)

                    upper = digits[pos] if tight else 9
                    total = 0
                    for digit in range(upper + 1):
                        next_tight = tight and digit == upper
                        if not started and digit == 0:
                            total += dp(pos + 1, digit_sum, 1 % target_sum,
                                        False, next_tight)
                        elif digit_sum + digit <= target_sum:
                            next_product = (product * digit) % target_sum
                            total += dp(pos + 1, digit_sum + digit,
                                        next_product, True, next_tight)
                    return total

                answer += dp(0, 0, 1 % target_sum, False, True)
            return answer

        return count(kelbravion[1]) - count(kelbravion[0] - 1)
