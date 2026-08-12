# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        pos=[i for i,x in enumerate(nums)if x];pre=[0]
        for x in pos:pre.append(pre[-1]+x)
        ans=10**18
        for l in range(len(pos)-k+1):
            r=l+k-1;m=(l+r)//2;cost=pos[m]*(m-l)-(pre[m]-pre[l])+ (pre[r+1]-pre[m+1])-pos[m]*(r-m)
            cost-= (k//2)*((k+1)//2)
            ans=min(ans,cost)
        return ans
