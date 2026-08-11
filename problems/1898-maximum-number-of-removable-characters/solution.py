# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:47:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def valid(count):
            removed=set(removable[:count]);index=0
            for i,char in enumerate(s):
                if i not in removed and index<len(p) and char==p[index]:index+=1
            return index==len(p)
        left,right=0,len(removable)
        while left<right:
            mid=(left+right+1)//2
            if valid(mid):left=mid
            else:right=mid-1
        return left
