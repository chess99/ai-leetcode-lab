# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:08Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        def count(a):
            m=len(a);n=len(a[0]);dp=[[0]*n for _ in range(m)];out=0
            for i in range(m-1,-1,-1):
                for j in range(n):
                    if a[i][j]:
                        dp[i][j]=1 if i==m-1 or j==0 or j==n-1 else 1+min(dp[i+1][j-1],dp[i+1][j],dp[i+1][j+1])
                        out+=dp[i][j]-1
            return out
        return count(grid)+count(grid[::-1])
