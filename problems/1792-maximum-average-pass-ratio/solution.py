# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:30Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap=[(-(p+1)/(t+1)+p/t,p,t) for p,t in classes];heapq.heapify(heap)
        for _ in range(extraStudents):
            _,p,t=heapq.heappop(heap);p+=1;t+=1;heapq.heappush(heap,(-(p+1)/(t+1)+p/t,p,t))
        return sum(p/t for _,p,t in heap)/len(heap)
