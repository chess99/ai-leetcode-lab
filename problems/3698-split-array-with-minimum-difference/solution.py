# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:48Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def splitArray(self, nums: List[int]) -> int:
        plomaresto = nums
        n = len(plomaresto)
        increasing = [True] * n
        decreasing = [True] * n
        for i in range(1, n):
            increasing[i] = increasing[i - 1] and nums[i - 1] < nums[i]
        for i in range(n - 2, -1, -1):
            decreasing[i] = decreasing[i + 1] and nums[i] > nums[i + 1]

        total = sum(nums)
        prefix = 0
        answer = None
        for i in range(n - 1):
            prefix += nums[i]
            if increasing[i] and decreasing[i + 1]:
                difference = abs(2 * prefix - total)
                answer = difference if answer is None else min(answer, difference)
        return -1 if answer is None else answer
