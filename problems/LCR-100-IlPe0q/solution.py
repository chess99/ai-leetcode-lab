# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:24Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1][:]
        for row in range(len(triangle) - 2, -1, -1):
            for column, value in enumerate(triangle[row]):
                dp[column] = value + min(dp[column], dp[column + 1])
        return dp[0]
