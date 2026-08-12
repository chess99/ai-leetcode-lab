# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:09Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        import heapq
        events = sorted([(l, -h, r) for l, r, h in buildings] + [(r, 0, 0) for l, r, h in buildings])
        heap = [(0, float("inf"))]; result = []
        for x, height, right in events:
            while heap[0][1] <= x: heapq.heappop(heap)
            if height: heapq.heappush(heap, (height, right))
            current = -heap[0][0]
            if not result or result[-1][1] != current: result.append([x, current])
        return result
