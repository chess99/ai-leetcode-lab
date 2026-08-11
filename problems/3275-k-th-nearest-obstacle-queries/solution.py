# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        import heapq

        heap = []
        answer = []
        for x, y in queries:
            heapq.heappush(heap, -(abs(x) + abs(y)))
            if len(heap) > k:
                heapq.heappop(heap)
            answer.append(-heap[0] if len(heap) == k else -1)
        return answer
