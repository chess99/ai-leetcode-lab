# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:09Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = prices[i] + min(dp[i + 1:min(n, 2 * i + 2) + 1])
        return dp[0]
