# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:50:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for total in range(1, target + 1):
            for value in nums:
                if value <= total: dp[total] += dp[total - value]
        return dp[target]
