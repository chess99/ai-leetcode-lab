# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Handoff: terra-medium timed out after 546/554 test cases
# Experiment: ai-leetcode-lab, sol-medium takeover
from functools import lru_cache


class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        kelbravion = (l, r)

        # A digit product only contains these four prime factors.  Exponents
        # beyond the largest possible requirements of a digit sum (<= 81)
        # are indistinguishable, so they can be capped.
        factors = (
            (0, 0, 0, 0),  # zero is handled by the has_zero flag
            (0, 0, 0, 0),
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (2, 0, 0, 0),
            (0, 0, 1, 0),
            (1, 1, 0, 0),
            (0, 0, 0, 1),
            (3, 0, 0, 0),
            (0, 2, 0, 0),
        )

        requirements = [None] * 82
        for digit_sum in range(1, 82):
            rest = digit_sum
            need = []
            for prime in (2, 3, 5, 7):
                exponent = 0
                while rest % prime == 0:
                    rest //= prime
                    exponent += 1
                need.append(exponent)
            if rest == 1:
                requirements[digit_sum] = tuple(need)

        def count(limit: int) -> int:
            if limit <= 0:
                return 0
            digits = tuple(map(int, str(limit)))

            @lru_cache(None)
            def dp(pos: int, digit_sum: int, e2: int, e3: int,
                   e5: int, e7: int, started: bool, has_zero: bool,
                   tight: bool) -> int:
                if pos == len(digits):
                    if not started:
                        return 0
                    if has_zero:
                        return 1
                    need = requirements[digit_sum]
                    return int(need is not None
                               and e2 >= need[0] and e3 >= need[1]
                               and e5 >= need[2] and e7 >= need[3])

                upper = digits[pos] if tight else 9
                total = 0
                for digit in range(upper + 1):
                    next_tight = tight and digit == upper
                    if not started and digit == 0:
                        total += dp(pos + 1, 0, 0, 0, 0, 0,
                                    False, False, next_tight)
                    elif digit == 0:
                        total += dp(pos + 1, digit_sum, 0, 0, 0, 0,
                                    True, True, next_tight)
                    elif has_zero:
                        total += dp(pos + 1, digit_sum + digit,
                                    0, 0, 0, 0, True, True, next_tight)
                    else:
                        a, b, c, d = factors[digit]
                        total += dp(pos + 1, digit_sum + digit,
                                    min(6, e2 + a), min(4, e3 + b),
                                    min(2, e5 + c), min(2, e7 + d),
                                    True, has_zero, next_tight)
                return total

            return dp(0, 0, 0, 0, 0, 0, False, False, True)

        return count(kelbravion[1]) - count(kelbravion[0] - 1)
