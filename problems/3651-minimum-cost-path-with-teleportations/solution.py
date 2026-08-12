# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:24Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0]);cells=sorted((grid[i][j],i,j)for i in range(m)for j in range(n));inf=10**18
        dp=[[[inf]*n for _ in range(m)]for _ in range(k+1)];dp[0][0][0]=0
        for t in range(k+1):
            best=inf;idx=0
            for i in range(m):
                for j in range(n):
                    if i:dp[t][i][j]=min(dp[t][i][j],dp[t][i-1][j]+grid[i][j])
                    if j:dp[t][i][j]=min(dp[t][i][j],dp[t][i][j-1]+grid[i][j])
            if t<k:
                for value,i,j in reversed(cells):
                    while idx<len(cells) and cells[-1-idx][0]>=value:
                        _,x,y=cells[-1-idx];best=min(best,dp[t][x][y]);idx+=1
                    dp[t+1][i][j]=min(dp[t+1][i][j],best)
        return min(dp[t][-1][-1]for t in range(k+1))
