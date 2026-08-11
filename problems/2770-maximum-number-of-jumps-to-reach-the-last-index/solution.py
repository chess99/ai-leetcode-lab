# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n=len(nums); dp=[-1]*n; dp[0]=0
        for i in range(n):
            if dp[i]>=0:
                for j in range(i+1,n):
                    if abs(nums[i]-nums[j])<=target: dp[j]=max(dp[j],dp[i]+1)
        return dp[-1]
