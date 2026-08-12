# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:24Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        difference = total + target
        if abs(target) > total or difference % 2:
            return 0
        positive = difference // 2
        dp = [0] * (positive + 1)
        dp[0] = 1
        for value in nums:
            for current in range(positive, value - 1, -1):
                dp[current] += dp[current - value]
        return dp[positive]
