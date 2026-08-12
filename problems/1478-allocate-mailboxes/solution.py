# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:57Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort();n=len(houses);dp=[0]+[10**9]*n
        for _ in range(k):
            nd=[0]+[10**9]*n
            for i in range(1,n+1):
                for j in range(i):nd[i]=min(nd[i],dp[j]+sum(abs(houses[t]-houses[(j+i-1)//2]) for t in range(j,i)))
            dp=nd
        return dp[n]
