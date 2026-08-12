# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:10:00Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts=[0]+sorted(cuts)+[n];m=len(cuts);dp=[[0]*m for _ in range(m)]
        for length in range(2,m):
            for i in range(m-length):
                j=i+length;dp[i][j]=min(dp[i][x]+dp[x][j]for x in range(i+1,j))+cuts[j]-cuts[i]
        return dp[0][-1]
