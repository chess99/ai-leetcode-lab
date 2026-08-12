# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:22Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
import heapq


class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        if n > 1 and k == 1:return -1.0
        full=(1<<n)-1; inf=float('inf');dist={(0,0,0):0.0};pq=[(0.0,0,0,0)]
        while pq:
            cost,mask,side,stage=heapq.heappop(pq)
            if cost!=dist[(mask,side,stage)]:continue
            if mask==full and side==1:return cost
            available=mask if side else full^mask
            sub=available
            if side:
                # Exactly one person returns.
                choices=[];x=available
                while x:
                    bit=x&-x;choices.append(bit);x-=bit
            else:
                choices=[];x=sub
                while x:
                    if x.bit_count()<=k:choices.append(x)
                    x=(x-1)&available
            for group in choices:
                people=[i for i in range(n)if group>>i&1]
                d=max(time[i]for i in people)*mul[stage];ns=(stage+int(d)%m)%m
                nm=mask^group;state=(nm,1-side,ns);nc=cost+d
                if nc<dist.get(state,inf):dist[state]=nc;heapq.heappush(pq,(nc,*state))
        return -1.0
