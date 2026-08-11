# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def possible(amount: int) -> bool:
            diff = [0] * (len(nums) + 1)
            for left, right, value in queries[:amount]:
                diff[left] += value
                diff[right + 1] -= value
            total = 0
            for i, need in enumerate(nums):
                total += diff[i]
                if total < need:
                    return False
            return True

        if not possible(len(queries)):
            return -1
        low, high = 0, len(queries)
        while low < high:
            mid = (low + high) // 2
            if possible(mid):
                high = mid
            else:
                low = mid + 1
        return low
