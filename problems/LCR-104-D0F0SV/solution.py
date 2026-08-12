# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:25Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for current in range(1, target + 1):
            for value in nums:
                if value <= current:
                    dp[current] += dp[current - value]
        return dp[target]
