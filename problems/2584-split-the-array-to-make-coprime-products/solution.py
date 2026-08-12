# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:35Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        def fac(x):
            p=2;out=[]
            while p*p<=x:
                if x%p==0:
                    out.append(p)
                    while x%p==0:x//=p
                p+=1
            return out+[x] if x>1 else out
        last={}
        for i,x in enumerate(nums):
            for p in fac(x):last[p]=i
        end=0
        for i,x in enumerate(nums[:-1]):
            for p in fac(x):end=max(end,last[p])
            if i==end:return i
        return -1
