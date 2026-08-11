# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:26Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def can_rob(capability: int) -> bool:
            count = index = 0
            while index < len(nums):
                if nums[index] <= capability:
                    count += 1
                    index += 2
                else:
                    index += 1
            return count >= k

        low, high = min(nums), max(nums)
        while low < high:
            middle = (low + high) // 2
            if can_rob(middle):
                high = middle
            else:
                low = middle + 1
        return low
