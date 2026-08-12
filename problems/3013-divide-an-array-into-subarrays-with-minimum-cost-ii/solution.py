# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:52Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        import heapq
        need=k-1;lo=[];hi=[];sumlo=0;chosen_size=0
        # The constraints are small enough for a value-indexed lazy heap scheme.
        chosen={};other={}
        def clean(heap,store,sign):
            while heap and store.get(sign*heap[0],0)==0:heapq.heappop(heap)
        def add(x):
            nonlocal sumlo,chosen_size
            if chosen_size<need or (lo and x<=-lo[0]):
                heapq.heappush(lo,-x);chosen[x]=chosen.get(x,0)+1;sumlo+=x;chosen_size+=1
            else:heapq.heappush(hi,x);other[x]=other.get(x,0)+1
            balance()
        def remove(x):
            nonlocal sumlo,chosen_size
            if chosen.get(x,0):chosen[x]-=1;sumlo-=x;chosen_size-=1
            else:other[x]-=1
            balance()
        def balance():
            nonlocal sumlo,chosen_size
            clean(lo,chosen,-1);clean(hi,other,1)
            while chosen_size>need:
                clean(lo,chosen,-1);x=-heapq.heappop(lo);chosen[x]-=1;other[x]=other.get(x,0)+1;heapq.heappush(hi,x);sumlo-=x;chosen_size-=1
            while chosen_size<need and hi:
                clean(hi,other,1)
                if not hi:break
                x=heapq.heappop(hi);other[x]-=1;chosen[x]=chosen.get(x,0)+1;heapq.heappush(lo,-x);sumlo+=x;chosen_size+=1
        ans=10**30
        for i in range(1,len(nums)):
            add(nums[i])
            if i>dist+1:remove(nums[i-dist-1])
            if i>=need:ans=min(ans,sumlo)
        return nums[0]+ans
