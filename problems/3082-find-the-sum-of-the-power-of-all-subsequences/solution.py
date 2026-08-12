# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        mod=10**9+7;dp=[0]*(k+1);dp[0]=1
        for x in nums:
            for s in range(k,-1,-1):
                dp[s]=(2*dp[s]+(dp[s-x] if s>=x else 0))%mod
        return dp[k]
