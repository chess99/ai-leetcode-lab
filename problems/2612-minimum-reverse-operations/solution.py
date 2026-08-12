# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:36Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        from collections import deque
        parent=[list(range(n+2)) for _ in range(2)]
        bad=set(banned)|{p}
        def find(par,x):
            if x>=n:return n
            if par[x]!=x:par[x]=find(par,par[x])
            return par[x]
        def erase(par,x):par[x]=find(par,x+2)
        for parity in range(2):
            for x in range(parity,n,2):
                if x in bad:erase(parent[parity],x)
        ans=[-1]*n;ans[p]=0;q=deque([p])
        while q:
            x=q.popleft();lo=max(0,x-k+1);hi=min(x,n-k);a=2*lo+k-1-x;b=2*hi+k-1-x
            par=parent[a%2];y=find(par,a)
            while y<=b:
                erase(par,y);ans[y]=ans[x]+1;q.append(y);y=find(par,y)
        return ans
