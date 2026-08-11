# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:24:04Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        suffix = [0] * (len(piles) + 1)
        for index in range(len(piles) - 1, -1, -1):
            suffix[index] = suffix[index + 1] + piles[index]

        @lru_cache(None)
        def best(index: int, m: int) -> int:
            if index + 2 * m >= len(piles):
                return suffix[index]
            return max(suffix[index] - best(index + taken, max(m, taken)) for taken in range(1, 2 * m + 1))

        return best(0, 1)
