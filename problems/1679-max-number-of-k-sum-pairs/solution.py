# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:29Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        operations = 0

        while left < right:
            pair_sum = nums[left] + nums[right]
            if pair_sum == k:
                operations += 1
                left += 1
                right -= 1
            elif pair_sum < k:
                left += 1
            else:
                right -= 1

        return operations
