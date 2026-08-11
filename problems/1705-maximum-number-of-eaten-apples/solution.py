# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:32Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap=[]; eaten=day=0
        while day<len(apples) or heap:
            if day<len(apples) and apples[day]:heapq.heappush(heap,(day+days[day],apples[day]))
            while heap and heap[0][0]<=day:heapq.heappop(heap)
            if heap:
                end,count=heapq.heappop(heap);eaten+=1
                if count>1:heapq.heappush(heap,(end,count-1))
            day+=1
        return eaten
