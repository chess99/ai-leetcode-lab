# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:11:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        difference = total - target
        if difference < 0 or difference % 2:
            return 0

        negative_sum = difference // 2
        ways = [0] * (negative_sum + 1)
        ways[0] = 1
        for number in nums:
            for current_sum in range(negative_sum, number - 1, -1):
                ways[current_sum] += ways[current_sum - number]
        return ways[negative_sum]
