# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        base=sum(nums);gain=sorted(((x^k)-x for x in nums),reverse=True)
        for i in range(0,len(gain)-1,2):
            if gain[i]+gain[i+1]>0:base+=gain[i]+gain[i+1]
        return base
