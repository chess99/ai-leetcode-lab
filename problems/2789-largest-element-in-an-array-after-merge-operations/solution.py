# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Created: 2026-08-15
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        merged = nums[-1]

        for value in reversed(nums[:-1]):
            if value <= merged:
                merged += value
            else:
                merged = value

        return merged
