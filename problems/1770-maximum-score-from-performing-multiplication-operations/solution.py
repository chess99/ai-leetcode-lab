# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:43Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m=len(multipliers);dp=[0]*(m+1)
        for i in range(m-1,-1,-1):
            nd=[0]*(m+1)
            for left in range(i+1):nd[left]=max(multipliers[i]*nums[left]+dp[left+1],multipliers[i]*nums[len(nums)-1-(i-left)]+dp[left])
            dp=nd
        return dp[0]
