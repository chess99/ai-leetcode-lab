# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:18:04Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        suffix_sum = nums[-1]
        suffix_length = 1
        result = 0

        for index in range(len(nums) - 2, -1, -1):
            if nums[index] * suffix_length > suffix_sum:
                result += 1
            suffix_sum += nums[index]
            suffix_length += 1

        return result
