# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        from collections import deque
        n=len(nums);pre=[0]
        for x in nums:pre.append(pre[-1]+x)
        neg=-10**30;dp=[0]*(n+1);ans=neg
        for _ in range(m):
            nd=[neg]*(n+1);q=deque()
            for i in range(1,n+1):
                x=i-l
                if x>=0:
                    while q and dp[q[-1]]-pre[q[-1]]<=dp[x]-pre[x]:q.pop()
                    q.append(x)
                while q and q[0]<i-r:q.popleft()
                nd[i]=max(nd[i-1],dp[i],pre[i]+(dp[q[0]]-pre[q[0]] if q else neg))
            dp=nd;ans=max(ans, max(dp))
        return ans
