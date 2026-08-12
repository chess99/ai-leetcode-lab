# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:42Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        from math import gcd
        g=[[]for _ in nums]
        for a,b in edges:g[a].append(b);g[b].append(a)
        stacks=[[]for _ in range(51)];ans=[-1]*len(nums)
        def dfs(u,p,d):
            best=(-1,-1)
            for v in range(1,51):
                if stacks[v]and gcd(v,nums[u])==1:best=max(best,stacks[v][-1])
            ans[u]=best[1];stacks[nums[u]].append((d,u))
            for v in g[u]:
                if v!=p:dfs(v,u,d+1)
            stacks[nums[u]].pop()
        dfs(0,-1,0);return ans
