# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:48Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0]);mod=10**9+7
        cells=sorted((grid[i][j],i,j) for i in range(m) for j in range(n))
        dp=[[1]*n for _ in range(m)]
        answer=0
        for value,x,y in cells:
            for a,b in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                if 0<=a<m and 0<=b<n and grid[a][b]<value:
                    dp[x][y]=(dp[x][y]+dp[a][b])%mod
            answer=(answer+dp[x][y])%mod
        return answer
