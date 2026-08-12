# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        from bisect import bisect_left
        jobs=sorted(zip(startTime,endTime,profit));starts=[x[0]for x in jobs];dp=[0]*(len(jobs)+1)
        for i in range(len(jobs)-1,-1,-1):dp[i]=max(dp[i+1],jobs[i][2]+dp[bisect_left(starts,jobs[i][1])])
        return dp[0]
