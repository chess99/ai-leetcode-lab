# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:47Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp=[[0]*(n+1)for _ in range(m+1)]
        for h,w,p in prices:dp[h][w]=max(dp[h][w],p)
        for h in range(1,m+1):
            for w in range(1,n+1):
                for x in range(1,h):dp[h][w]=max(dp[h][w],dp[x][w]+dp[h-x][w])
                for x in range(1,w):dp[h][w]=max(dp[h][w],dp[h][x]+dp[h][w-x])
        return dp[m][n]
