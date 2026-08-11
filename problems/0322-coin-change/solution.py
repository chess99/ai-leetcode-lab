# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:47:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1); dp[0]=0
        for total in range(1,amount+1):
            dp[total]=min((dp[total-coin]+1 for coin in coins if coin<=total),default=amount+1)
        return -1 if dp[amount]>amount else dp[amount]
