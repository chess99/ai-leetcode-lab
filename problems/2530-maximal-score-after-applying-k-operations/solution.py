# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:25Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-value for value in nums]
        heapq.heapify(heap)
        score = 0
        for _ in range(k):
            value = -heapq.heappop(heap)
            score += value
            heapq.heappush(heap, -((value + 2) // 3))
        return score
