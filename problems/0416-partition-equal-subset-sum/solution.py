# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:53:28Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        possible = [False] * (target + 1)
        possible[0] = True
        for value in nums:
            for amount in range(target, value - 1, -1):
                possible[amount] = possible[amount] or possible[amount - value]
        return possible[target]
