# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:51:58Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n=len(dist);dp=[10**30]*(n+1);dp[0]=0
        for i,distance in enumerate(dist):
            following=[10**30]*(n+1)
            for skips in range(i+1):
                travel=dp[skips]+distance
                following[skips+1]=min(following[skips+1],travel)
                following[skips]=min(following[skips],travel if i==n-1 else ((travel+speed-1)//speed)*speed)
            dp=following
        limit=hoursBefore*speed
        return next((i for i,value in enumerate(dp) if value<=limit),-1)
