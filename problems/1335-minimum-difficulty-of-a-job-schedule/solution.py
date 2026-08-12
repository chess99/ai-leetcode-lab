# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:50Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n=len(jobDifficulty)
        if n<d:return -1
        dp=[float('inf')]*(n+1);dp[0]=0
        for day in range(1,d+1):
            following=[float('inf')]*(n+1)
            for end in range(day,n+1):
                hardest=0
                for start in range(end-1,day-2,-1):hardest=max(hardest,jobDifficulty[start]);following[end]=min(following[end],dp[start]+hardest)
            dp=following
        return dp[n]
