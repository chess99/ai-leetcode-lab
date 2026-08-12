# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low, high = max(nums), sum(nums)
        while low < high:
            limit = (low + high) // 2
            groups, current = 1, 0
            for value in nums:
                if current + value > limit:
                    groups += 1
                    current = value
                else:
                    current += value
            if groups <= k:
                high = limit
            else:
                low = limit + 1
        return low
