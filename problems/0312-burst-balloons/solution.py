# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        values = [1] + [value for value in nums if value] + [1]
        size = len(values)
        dp = [[0] * size for _ in range(size)]
        for width in range(2, size):
            for left in range(size - width):
                right = left + width
                dp[left][right] = max(
                    dp[left][middle] + dp[middle][right]
                    + values[left] * values[middle] * values[right]
                    for middle in range(left + 1, right)
                )
        return dp[0][-1]
