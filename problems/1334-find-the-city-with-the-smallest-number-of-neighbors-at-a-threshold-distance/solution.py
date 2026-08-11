# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:41:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        inf = float('inf'); dist = [[inf] * n for _ in range(n)]
        for i in range(n): dist[i][i] = 0
        for a,b,w in edges: dist[a][b] = dist[b][a] = w
        for mid in range(n):
            for start in range(n):
                for end in range(n): dist[start][end] = min(dist[start][end], dist[start][mid] + dist[mid][end])
        return min(range(n), key=lambda city: (sum(distance <= distanceThreshold for distance in dist[city]) - 1, -city))
