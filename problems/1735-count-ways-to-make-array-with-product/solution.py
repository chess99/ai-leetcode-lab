# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        from math import comb
        mod=10**9+7;ans=[]
        for n,x in queries:
            r=1;d=2
            while d*d<=x:
                c=0
                while x%d==0:x//=d;c+=1
                r=r*comb(n+c-1,c)%mod;d+=1
            if x>1:r=r*n%mod
            ans.append(r)
        return ans
