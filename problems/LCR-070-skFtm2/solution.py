# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if middle % 2:
                middle -= 1
            if nums[middle] == nums[middle + 1]:
                left = middle + 2
            else:
                right = middle
        return nums[left]
