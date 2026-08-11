# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:26Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        small, large = 0, (len(nums) + 1) // 2
        pairs = 0
        while small < len(nums) // 2 and large < len(nums):
            if nums[small] * 2 <= nums[large]:
                pairs += 1
                small += 1
            large += 1
        return pairs * 2
