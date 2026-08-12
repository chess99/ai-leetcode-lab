# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:51Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n=len(nums);p=list(range(n));sm=nums[:];on=[False]*n;ans=[0]*n;best=0
        def find(x):
            while p[x]!=x:p[x]=p[p[x]];x=p[x]
            return x
        for i in range(n-1,-1,-1):
            ans[i]=best;x=removeQueries[i];on[x]=True
            for y in (x-1,x+1):
                if 0<=y<n and on[y]:
                    a,b=find(x),find(y);p[a]=b;sm[b]+=sm[a]
            best=max(best,sm[find(x)])
        return ans
