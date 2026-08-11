# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:01:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        candidates = []
        for index, value in enumerate(nums):
            if not candidates or value < nums[candidates[-1]]:
                candidates.append(index)

        widest = 0
        for right in range(len(nums) - 1, -1, -1):
            while candidates and nums[candidates[-1]] <= nums[right]:
                widest = max(widest, right - candidates.pop())
        return widest
