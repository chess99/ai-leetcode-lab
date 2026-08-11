# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:16Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        rows, cols = len(moveTime), len(moveTime[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]
        while heap:
            time, r, c = heapq.heappop(heap)
            if (r, c) == (rows - 1, cols - 1):
                return time
            if time != dist[r][c]:
                continue
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    cost = 1 if (nr + nc) % 2 else 2
                    arrival = max(time, moveTime[nr][nc]) + cost
                    if arrival < dist[nr][nc]:
                        dist[nr][nc] = arrival
                        heapq.heappush(heap, (arrival, nr, nc))
        return -1
