# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda edge: edge[2]);p=list(range(n))
        def f(x):
            while p[x]!=x:p[x]=p[p[x]];x=p[x]
            return x
        ans=[False]*len(queries);i=0
        for u,v,l,idx in sorted([q+[j]for j,q in enumerate(queries)],key=lambda x:x[2]):
            while i<len(edgeList) and edgeList[i][2]<l:
                a,b,_=edgeList[i];p[f(a)]=f(b);i+=1
            ans[idx]=f(u)==f(v)
        return ans
