# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:59Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache
from typing import List


class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        full_mask = (1 << size) - 1

        @lru_cache(None)
        def minimum_cost(mask, last):
            if mask == full_mask:
                return abs(last - nums[0])
            best = 10 ** 9
            for following in range(1, size):
                if mask >> following & 1 == 0:
                    candidate = (abs(last - nums[following])
                                 + minimum_cost(mask | 1 << following, following))
                    best = min(best, candidate)
            return best

        permutation = [0]
        mask = 1
        last = 0
        while mask != full_mask:
            optimal = minimum_cost(mask, last)
            for following in range(1, size):
                if (mask >> following & 1 == 0
                        and abs(last - nums[following])
                        + minimum_cost(mask | 1 << following, following) == optimal):
                    permutation.append(following)
                    mask |= 1 << following
                    last = following
                    break
        return permutation
