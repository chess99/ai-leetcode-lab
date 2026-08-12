# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:52Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        choices = len(slices) // 3

        def linear(values):
            dp = [[0] * (choices + 1) for _ in range(len(values) + 1)]
            for length in range(1, len(values) + 1):
                for count in range(1, min(choices, (length + 1) // 2) + 1):
                    take = values[length - 1]
                    if length >= 2:
                        take += dp[length - 2][count - 1]
                    dp[length][count] = max(dp[length - 1][count], take)
            return dp[-1][choices]

        return max(linear(slices[:-1]), linear(slices[1:]))
