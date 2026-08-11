# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        minimum = maximum = 0
        for right in range(indexDifference, len(nums)):
            candidate = right - indexDifference
            if nums[candidate] < nums[minimum]:
                minimum = candidate
            if nums[candidate] > nums[maximum]:
                maximum = candidate
            if abs(nums[right] - nums[minimum]) >= valueDifference:
                return [minimum, right]
            if abs(nums[right] - nums[maximum]) >= valueDifference:
                return [maximum, right]
        return [-1, -1]
