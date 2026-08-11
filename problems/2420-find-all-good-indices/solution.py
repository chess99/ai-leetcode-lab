# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n=len(nums); down=[1]*n; up=[1]*n
        for i in range(1,n): down[i]=down[i-1]+1 if nums[i-1]>=nums[i] else 1
        for i in range(n-2,-1,-1): up[i]=up[i+1]+1 if nums[i]<=nums[i+1] else 1
        return [i for i in range(k,n-k) if down[i-1]>=k and up[i+1]>=k]
