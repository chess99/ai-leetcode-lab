# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        delta=[0]*(len(nums)+1); active=0
        for i,x in enumerate(nums):
            active+=delta[i]; need=x-active
            if need<0 or (need and i+k>len(nums)): return False
            if need:
                active+=need; delta[i+k]-=need
        return True
