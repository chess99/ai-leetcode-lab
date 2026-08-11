# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        rounds, remainder = divmod(target, total)
        if remainder == 0:
            return rounds * len(nums)
        left = current = 0
        best = float("inf")
        doubled = nums * 2
        for right, value in enumerate(doubled):
            current += value
            while current > remainder:
                current -= doubled[left]
                left += 1
            if current == remainder:
                best = min(best, right - left + 1)
        return -1 if best == float("inf") else rounds * len(nums) + best
