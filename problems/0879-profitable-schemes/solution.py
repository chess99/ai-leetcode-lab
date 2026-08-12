# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod=1_000_000_007;dp=[[0]*(minProfit+1) for _ in range(n+1)];dp[0][0]=1
        for people,gain in zip(group,profit):
            for used in range(n,people-1,-1):
                for earned in range(minProfit,-1,-1):dp[used][min(minProfit,earned+gain)]=(dp[used][min(minProfit,earned+gain)]+dp[used-people][earned])%mod
        return sum(dp[used][minProfit] for used in range(n+1))%mod
