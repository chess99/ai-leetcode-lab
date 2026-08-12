# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        from bisect import bisect_left
        pos={x:i for i,x in enumerate(target)};a=[]
        for x in arr:
            if x in pos:
                i=bisect_left(a,pos[x])
                if i==len(a):a.append(pos[x])
                else:a[i]=pos[x]
        return len(target)-len(a)
