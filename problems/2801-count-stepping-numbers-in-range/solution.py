# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:41Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache


class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        modulus = 1_000_000_007

        def count(bound):
            @lru_cache(None)
            def dynamic(index, previous, tight, started):
                if index == len(bound):
                    return int(started)
                maximum = int(bound[index]) if tight else 9
                total = 0
                for digit in range(maximum + 1):
                    next_tight = tight and digit == maximum
                    if not started and digit == 0:
                        total += dynamic(index + 1, 10, next_tight, False)
                    elif not started or abs(previous - digit) == 1:
                        total += dynamic(index + 1, digit, next_tight, True)
                return total % modulus
            return dynamic(0, 10, True, False)

        low_is_stepping = all(abs(int(low[i]) - int(low[i - 1])) == 1
                              for i in range(1, len(low)))
        return (count(high) - count(low) + low_is_stepping) % modulus
