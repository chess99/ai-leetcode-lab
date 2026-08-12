# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:36Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from functools import lru_cache
from typing import List
class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        counts=list(Counter(nums).values());m=len(quantity);sums=[0]*(1<<m)
        for mask in range(1,1<<m):bit=mask&-mask;sums[mask]=sums[mask^bit]+quantity[bit.bit_length()-1]
        @lru_cache(None)
        def assign(index,mask):
            if mask==0:return True
            if index==len(counts):return False
            subset=mask
            while subset:
                if sums[subset]<=counts[index] and assign(index+1,mask^subset):return True
                subset=(subset-1)&mask
            return assign(index+1,mask)
        return assign(0,(1<<m)-1)
