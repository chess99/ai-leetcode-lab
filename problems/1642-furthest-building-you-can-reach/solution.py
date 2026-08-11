# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:26Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        climbs=[]
        for index in range(len(heights)-1):
            climb=heights[index+1]-heights[index]
            if climb>0:
                heapq.heappush(climbs,climb)
                if len(climbs)>ladders:bricks-=heapq.heappop(climbs)
                if bricks<0:return index
        return len(heights)-1
