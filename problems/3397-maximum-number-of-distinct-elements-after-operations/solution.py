# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        next_free = -10**30
        count = 0
        for value in sorted(nums):
            chosen = max(value - k, next_free)
            if chosen <= value + k:
                count += 1
                next_free = chosen + 1
        return count
