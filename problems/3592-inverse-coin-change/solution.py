# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        n=len(numWays); dp=[1]+[0]*n; coins=[]
        for coin in range(1,n+1):
            target=numWays[coin-1]
            if dp[coin]>target: return []
            if dp[coin]<target:
                coins.append(coin)
                for total in range(coin,n+1): dp[total]+=dp[total-coin]
        return coins if dp[1:]==numWays else []
