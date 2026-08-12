# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:33Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available=list(range(k));busy=[];count=[0]*k
        for i,(start,duration) in enumerate(zip(arrival,load)):
            while busy and busy[0][0]<=start:
                _,server=heapq.heappop(busy);heapq.heappush(available,i+(server-i)%k)
            if not available:continue
            server=heapq.heappop(available)%k;count[server]+=1;heapq.heappush(busy,(start+duration,server))
        best=max(count);return [i for i,value in enumerate(count) if value==best]
