# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:11Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List
class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        roads=[(x1,y1,x2,y2,min(cost,abs(x1-x2)+abs(y1-y2))) for x1,y1,x2,y2,cost in specialRoads]
        dist={(start[0],start[1]):0}; heap=[(0,start[0],start[1])]; ans=abs(start[0]-target[0])+abs(start[1]-target[1])
        while heap:
            d,x,y=heapq.heappop(heap)
            if d!=dist[(x,y)]: continue
            ans=min(ans,d+abs(x-target[0])+abs(y-target[1]))
            for x1,y1,x2,y2,cost in roads:
                nd=d+abs(x-x1)+abs(y-y1)+cost
                if nd<dist.get((x2,y2),float('inf')): dist[(x2,y2)]=nd; heapq.heappush(heap,(nd,x2,y2))
        return ans
