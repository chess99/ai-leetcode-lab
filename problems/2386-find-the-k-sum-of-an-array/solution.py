# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:51Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        import heapq
        base=sum(x for x in nums if x>0);a=sorted(map(abs,nums))
        if k==1:return base
        q=[(a[0],0)]
        for _ in range(k-2):
            x,i=heapq.heappop(q)
            if i+1<len(a):heapq.heappush(q,(x+a[i+1],i+1));heapq.heappush(q,(x-a[i]+a[i+1],i+1))
        return base-q[0][0]
