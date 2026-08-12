# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        from math import gcd
        if len(nums)==1:return True
        if 1 in nums:return False
        parent=list(range(len(nums)))
        def find(x):
            while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
            return x
        owner={}
        for i,x in enumerate(nums):
            p=2
            while p*p<=x:
                if x%p==0:
                    if p in owner:parent[find(i)]=find(owner[p])
                    owner[p]=i
                    while x%p==0:x//=p
                p+=1
            if x>1:
                if x in owner:parent[find(i)]=find(owner[x])
                owner[x]=i
        return len({find(i)for i in range(len(nums))})==1
