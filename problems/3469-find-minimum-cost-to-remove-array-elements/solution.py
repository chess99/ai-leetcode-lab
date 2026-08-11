# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:19Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from functools import lru_cache
class Solution:
    def minCost(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dp(i,carry):
            if i>=len(nums): return carry
            if i==len(nums)-1: return max(carry,nums[i])
            a,b,c=carry,nums[i],nums[i+1]
            return min(max(a,b)+dp(i+2,c),max(a,c)+dp(i+2,b),max(b,c)+dp(i+2,a))
        if len(nums)<3:return max(nums)
        a,b,c=nums[:3]
        return min(max(a,b)+dp(3,c),max(a,c)+dp(3,b),max(b,c)+dp(3,a))
