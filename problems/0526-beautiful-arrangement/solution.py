# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:14:02Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache


class Solution:
    def countArrangement(self, n: int) -> int:
        @lru_cache(None)
        def count(used_mask: int) -> int:
            position = used_mask.bit_count() + 1
            if position > n:
                return 1

            arrangements = 0
            for value in range(1, n + 1):
                bit = 1 << (value - 1)
                if not used_mask & bit and (
                    value % position == 0 or position % value == 0
                ):
                    arrangements += count(used_mask | bit)
            return arrangements

        return count(0)
