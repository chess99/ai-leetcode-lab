# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:50:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort(); dp=[1]*len(nums); prev=[-1]*len(nums); best=0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j]==0 and dp[j]+1>dp[i]: dp[i],prev[i]=dp[j]+1,j
            if dp[i]>dp[best]: best=i
        result=[]
        while best!=-1: result.append(nums[best]); best=prev[best]
        return result
