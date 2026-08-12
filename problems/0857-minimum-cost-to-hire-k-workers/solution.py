# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:54Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers=sorted((w/q,q) for q,w in zip(quality,wage));heap=[];total=0;answer=float('inf')
        for ratio,q in workers:
            heapq.heappush(heap,-q);total+=q
            if len(heap)>k:total+=heapq.heappop(heap)
            if len(heap)==k:answer=min(answer,total*ratio)
        return answer
