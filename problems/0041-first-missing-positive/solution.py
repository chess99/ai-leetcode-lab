# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:24:53Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        for index in range(length):
            while (1 <= nums[index] <= length
                   and nums[nums[index] - 1] != nums[index]):
                target = nums[index] - 1
                nums[index], nums[target] = nums[target], nums[index]
        for index, value in enumerate(nums):
            if value != index + 1:
                return index + 1
        return length + 1
