# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Created: 2026-08-13
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        offset = 10_000
        counts = [0] * 20_001

        for value in nums:
            counts[value + offset] += 1

        remaining = k
        for index in range(20_000, -1, -1):
            remaining -= counts[index]
            if remaining <= 0:
                return index - offset
