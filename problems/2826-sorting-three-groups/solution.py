# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:06Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        for x in nums:
            old = dp[:]
            dp = [min(old[:g+1]) + (x != g + 1) for g in range(3)]
        return min(dp)
