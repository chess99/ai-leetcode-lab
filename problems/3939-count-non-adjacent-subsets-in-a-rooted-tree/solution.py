# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def countValidSubsets(self, parent: List[int], nums: List[int], k: int) -> int:
        mod=1_000_000_007;n=len(nums);g=[[]for _ in range(n)]
        for i in range(1,n):g[parent[i]].append(i)
        def dfs(u):
            no=[0]*k;yes=[0]*k;no[0]=1;yes[nums[u]%k]=1
            for v in g[u]:
                a,b=dfs(v);both=[(a[i]+b[i])%mod for i in range(k)]
                def merge(x,y):
                    z=[0]*k
                    for i,p in enumerate(x):
                        if p:
                            for j,q in enumerate(y):z[(i+j)%k]=(z[(i+j)%k]+p*q)%mod
                    return z
                no=merge(no,both);yes=merge(yes,a)
            return no,yes
        a,b=dfs(0);return (a[0]+b[0]-1)%mod
