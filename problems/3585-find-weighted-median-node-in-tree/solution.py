# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:22Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        g=[[]for _ in range(n)]
        for a,b,w in edges:g[a].append((b,w));g[b].append((a,w))
        lg=(n+1).bit_length();up=[[0]*n for _ in range(lg)];jump=[[0]*n for _ in range(lg)];dep=[0]*n;dist=[0]*n;order=[0]
        for u in order:
            for v,w in g[u]:
                if v!=up[0][u]:up[0][v]=u;jump[0][v]=w;dep[v]=dep[u]+1;dist[v]=dist[u]+w;order.append(v)
        for p in range(1,lg):
            for v in range(n):up[p][v]=up[p-1][up[p-1][v]];jump[p][v]=jump[p-1][v]+jump[p-1][up[p-1][v]]
        def lca(a,b):
            if dep[a]<dep[b]:a,b=b,a
            for p in range(lg):
                if (dep[a]-dep[b])>>p&1:a=up[p][a]
            if a==b:return a
            for p in range(lg-1,-1,-1):
                if up[p][a]!=up[p][b]:a,b=up[p][a],up[p][b]
            return up[0][a]
        def climb(u,need):
            got=0
            for p in range(lg-1,-1,-1):
                if got+jump[p][u]<need:got+=jump[p][u];u=up[p][u]
            return up[0][u]
        ans=[]
        for u,v in queries:
            if u == v:
                ans.append(u); continue
            z=lca(u,v);total=dist[u]+dist[v]-2*dist[z];need=(total+1)//2
            if dist[u]-dist[z]>=need:ans.append(climb(u,need))
            else:
                # The desired point lies on the LCA-to-v suffix.  Climb from
                # v as far as possible while staying within floor(total / 2).
                limit=total-need; got=0; cur=v
                for p in range(lg-1,-1,-1):
                    if got+jump[p][cur]<=limit:
                        got+=jump[p][cur];cur=up[p][cur]
                ans.append(cur)
        return ans
