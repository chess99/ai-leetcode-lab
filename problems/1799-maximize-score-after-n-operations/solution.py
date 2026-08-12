# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:45Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache
from math import gcd
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        full = (1 << len(nums)) - 1

        @lru_cache(None)
        def search(mask):
            if mask == full:
                return 0
            operation = mask.bit_count() // 2 + 1
            answer = 0
            for first in range(len(nums)):
                if mask >> first & 1:
                    continue
                for second in range(first + 1, len(nums)):
                    if mask >> second & 1 == 0:
                        answer = max(answer,
                                     operation * gcd(nums[first], nums[second]) +
                                     search(mask | 1 << first | 1 << second))
            return answer

        return search(0)
