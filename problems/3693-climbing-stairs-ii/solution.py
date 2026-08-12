# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:47Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        keldoniraq = costs
        dp = [0] + [10**30] * n
        for stair in range(1, n + 1):
            dp[stair] = keldoniraq[stair - 1] + min(
                dp[previous] + (stair - previous) ** 2
                for previous in range(max(0, stair - 3), stair)
            )
        return dp[n]
