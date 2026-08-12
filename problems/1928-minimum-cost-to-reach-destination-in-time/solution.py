# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:00Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n=len(passingFees);dp=[[10**9]*n for _ in range(maxTime+1)];dp[0][0]=passingFees[0]
        for time in range(1,maxTime+1):
            for a,b,cost in edges:
                if cost<=time:
                    dp[time][a]=min(dp[time][a],dp[time-cost][b]+passingFees[a]);dp[time][b]=min(dp[time][b],dp[time-cost][a]+passingFees[b])
        answer=min(row[-1] for row in dp);return -1 if answer>=10**9 else answer
