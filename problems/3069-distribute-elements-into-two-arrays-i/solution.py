# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:41:43Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        first = [nums[0]]
        second = [nums[1]]
        for value in nums[2:]:
            if first[-1] > second[-1]:
                first.append(value)
            else:
                second.append(value)
        return first + second
