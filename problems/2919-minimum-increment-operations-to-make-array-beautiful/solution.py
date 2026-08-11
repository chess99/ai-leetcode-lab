# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:08Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        first = second = third = 0
        for value in nums:
            first, second, third = second, third, max(0, k - value) + min(first, second, third)
        return min(first, second, third)
