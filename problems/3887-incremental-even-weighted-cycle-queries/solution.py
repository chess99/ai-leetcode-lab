# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:35Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def numberOfEdgesAdded(self, n: int, edges: List[List[int]]) -> int:
        p=list(range(n));xr=[0]*n;sz=[1]*n
        def find(x):
            if p[x]!=x:
                r,v=find(p[x]);xr[x]^=v;p[x]=r
            return p[x],xr[x]
        ans=0
        for a,b,w in edges:
            ra,xa=find(a);rb,xb=find(b)
            if ra==rb:
                ans+=xa^xb==w
            else:
                if sz[ra]<sz[rb]:ra,rb,xa,xb=rb,ra,xb,xa
                p[rb]=ra;xr[rb]=xa^xb^w;sz[ra]+=sz[rb];ans+=1
        return ans
