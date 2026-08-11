# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:08Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap=[-value for value in piles];heapq.heapify(heap)
        for _ in range(k):
            value=-heapq.heappop(heap);heapq.heappush(heap,-((value+1)//2))
        return -sum(heap)
