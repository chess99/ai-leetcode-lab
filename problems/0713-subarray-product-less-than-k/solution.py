# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:33:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        product = 1
        left = 0
        count = 0
        for right, number in enumerate(nums):
            product *= number
            while product >= k:
                product //= nums[left]
                left += 1
            count += right - left + 1
        return count
