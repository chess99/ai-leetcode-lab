# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:43:09Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        @lru_cache(maxsize=None)
        def power(value: int) -> int:
            if value == 1:
                return 0
            if value % 2 == 0:
                return 1 + power(value // 2)
            return 1 + power(3 * value + 1)

        ordered_values = sorted(range(lo, hi + 1), key=lambda value: (power(value), value))
        return ordered_values[k - 1]
