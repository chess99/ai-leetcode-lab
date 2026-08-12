# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:42Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache


class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def count(bound):
            if bound <= 0:
                return 0
            digits = str(bound)

            @lru_cache(None)
            def dynamic(index, remainder, balance, tight, started):
                if index == len(digits):
                    return int(started and remainder == 0 and balance == 0)
                maximum = int(digits[index]) if tight else 9
                answer = 0
                for digit in range(maximum + 1):
                    next_tight = tight and digit == maximum
                    if not started and digit == 0:
                        answer += dynamic(index + 1, 0, 0, next_tight, False)
                    else:
                        next_balance = balance + (1 if digit & 1 else -1)
                        answer += dynamic(index + 1,
                                          (remainder * 10 + digit) % k,
                                          next_balance, next_tight, True)
                return answer

            return dynamic(0, 0, 0, True, False)

        return count(high) - count(low - 1)
