# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:58:10Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        mod=10**9+7;count={};sm={}
        for x in nums:
            c=(count.get(x-1,0)+count.get(x+1,0)+1)%mod
            v=(sm.get(x-1,0)+sm.get(x+1,0)+x*c)%mod
            count[x]=(count.get(x,0)+c)%mod;sm[x]=(sm.get(x,0)+v)%mod
        return sum(sm.values())%mod
