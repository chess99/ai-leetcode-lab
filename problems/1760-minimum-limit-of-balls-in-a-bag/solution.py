# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:27Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        low, high = 1, max(nums)

        while low < high:
            limit = (low + high) // 2
            required_operations = sum((balls - 1) // limit for balls in nums)
            if required_operations <= maxOperations:
                high = limit
            else:
                low = limit + 1

        return low
