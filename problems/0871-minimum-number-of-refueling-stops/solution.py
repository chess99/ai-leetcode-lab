# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:55Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        heap=[];fuel=startFuel;index=stops=0
        while fuel<target:
            while index<len(stations) and stations[index][0]<=fuel:heapq.heappush(heap,-stations[index][1]);index+=1
            if not heap:return -1
            fuel-=heapq.heappop(heap);stops+=1
        return stops
