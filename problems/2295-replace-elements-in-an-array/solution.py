# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:24Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        positions = {value: index for index, value in enumerate(nums)}

        for old_value, new_value in operations:
            index = positions.pop(old_value)
            nums[index] = new_value
            positions[new_value] = index

        return nums
