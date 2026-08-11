# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:11:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [-1] * length
        stack = []
        for index in range(2 * length):
            current_index = index % length
            while stack and nums[stack[-1]] < nums[current_index]:
                result[stack.pop()] = nums[current_index]
            if index < length:
                stack.append(current_index)
        return result
