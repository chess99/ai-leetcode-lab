# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        first={}
        for i,x in enumerate(elements): first.setdefault(x,i)
        ans=[]
        for value in groups:
            best=10**9; d=1
            while d*d<=value:
                if value%d==0:
                    best=min(best,first.get(d,best),first.get(value//d,best))
                d+=1
            ans.append(best if best<10**9 else -1)
        return ans
