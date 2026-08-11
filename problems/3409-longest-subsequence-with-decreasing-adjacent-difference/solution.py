# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        max_value = max(nums)
        dp = [[0] * (max_value + 1) for _ in range(max_value + 1)]
        best = 1
        for value in nums:
            for previous in range(1, max_value + 1):
                diff = abs(value - previous)
                candidate = 1 + dp[previous][diff]
                if candidate > dp[value][diff]:
                    dp[value][diff] = candidate
                    best = max(best, candidate)
            for diff in range(max_value - 1, -1, -1):
                dp[value][diff] = max(dp[value][diff], dp[value][diff + 1], 1)
        return best
