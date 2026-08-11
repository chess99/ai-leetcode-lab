# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        best = nums[0]
        for mask in range(1, 1 << len(nums)):
            product = 1
            for index, value in enumerate(nums):
                if mask >> index & 1:
                    product *= value
            best = max(best, product)
        return best
