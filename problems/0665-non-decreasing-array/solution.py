# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:29:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changes = 0
        for index in range(1, len(nums)):
            if nums[index - 1] <= nums[index]:
                continue
            changes += 1
            if changes > 1:
                return False
            if index >= 2 and nums[index - 2] > nums[index]:
                nums[index] = nums[index - 1]
            else:
                nums[index - 1] = nums[index]
        return True
