# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:07Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [-10**9] * (target + 1)
        dp[0] = 0
        for value in nums:
            for total in range(target, value - 1, -1):
                dp[total] = max(dp[total], dp[total - value] + 1)
        return dp[target] if dp[target] >= 0 else -1
