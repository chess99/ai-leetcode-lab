# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0] * (len(nums) + 1)
        for left, right in queries:
            diff[left] += 1
            diff[right + 1] -= 1
        coverage = 0
        for i, value in enumerate(nums):
            coverage += diff[i]
            if coverage < value:
                return False
        return True
