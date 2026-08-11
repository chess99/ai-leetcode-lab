# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:27:46Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = largest = smallest = nums[0]
        for value in nums[1:]:
            if value < 0:
                largest, smallest = smallest, largest
            largest = max(value, largest * value)
            smallest = min(value, smallest * value)
            best = max(best, largest)
        return best
