# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:06Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp=points[0]
        for row in points[1:]:
            left=[];best=-10**18
            for j,value in enumerate(dp):best=max(best,value+j);left.append(best-j)
            right=[0]*len(dp);best=-10**18
            for j in range(len(dp)-1,-1,-1):best=max(best,dp[j]-j);right[j]=best+j
            dp=[value+max(left[j],right[j]) for j,value in enumerate(row)]
        return max(dp)
