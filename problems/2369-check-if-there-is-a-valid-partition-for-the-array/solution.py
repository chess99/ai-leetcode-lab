# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:08Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        valid = [False] * (len(nums) + 1)
        valid[0] = True
        for end in range(2, len(nums) + 1):
            if nums[end - 1] == nums[end - 2] and valid[end - 2]:
                valid[end] = True
            if end >= 3 and valid[end - 3]:
                equal_three = nums[end - 3] == nums[end - 2] == nums[end - 1]
                consecutive = nums[end - 3] + 1 == nums[end - 2] and nums[end - 2] + 1 == nums[end - 1]
                if equal_three or consecutive:
                    valid[end] = True
        return valid[-1]
