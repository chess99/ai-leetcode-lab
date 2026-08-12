# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        from collections import deque
        if source == target:
            return 0
        g=[[]for _ in range(n)];vals=[]
        for a,b,w in edges:g[a].append((b,w));g[b].append((a,w));vals.append(w)
        def ok(t):
            d=[10**9]*n;d[source]=0;q=deque([source])
            while q:
                u=q.popleft()
                for v,w in g[u]:
                    z=d[u]+(w>t)
                    if z<d[v]:
                        d[v]=z
                        (q.appendleft if w<=t else q.append)(v)
            return d[target]<=k
        vals=sorted(set(vals));lo=0;hi=len(vals)-1;ans=-1
        while lo<=hi:
            mid=(lo+hi)//2
            if ok(vals[mid]):ans=vals[mid];hi=mid-1
            else:lo=mid+1
        return ans
