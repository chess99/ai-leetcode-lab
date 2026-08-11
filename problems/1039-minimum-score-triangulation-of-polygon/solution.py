# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:12:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        size = len(values)
        dp = [[0] * size for _ in range(size)]
        for length in range(3, size + 1):
            for left in range(size - length + 1):
                right = left + length - 1
                dp[left][right] = min(
                    dp[left][middle] + values[left] * values[middle] * values[right] + dp[middle][right]
                    for middle in range(left + 1, right)
                )
        return dp[0][-1]
