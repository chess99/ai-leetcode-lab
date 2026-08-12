# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:48Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n=len(nums);g=[[]for _ in nums]
        for a,b in edges:g[a].append(b);g[b].append(a)
        tin=[0]*n;tout=[0]*n;xor=nums[:];parent=[-1]*n;order=[]
        stack=[(0,False)];timer=0
        while stack:
            u,leaving=stack.pop()
            if leaving:
                tout[u]=timer
                continue
            tin[u]=timer;timer+=1;order.append(u);stack.append((u,True))
            for v in reversed(g[u]):
                if v!=parent[u]:parent[v]=u;stack.append((v,False))
        for u in reversed(order[1:]):xor[parent[u]]^=xor[u]
        total=xor[0];ans=10**9
        for a in range(1,n):
            for b in range(1,a):
                if tin[a]<=tin[b]<tout[a]:x,y=xor[b],xor[a]^xor[b]
                elif tin[b]<=tin[a]<tout[b]:x,y=xor[a],xor[b]^xor[a]
                else:x,y=xor[a],xor[b]
                ans=min(ans,max(x,y,total^x^y)-min(x,y,total^x^y))
        return ans
