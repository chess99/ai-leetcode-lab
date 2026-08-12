# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:36Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        import heapq
        m,n=len(grid),len(grid[0]);rows=[[]for _ in range(m)];cols=[[]for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if i==j==0:d=1
                else:
                    while rows[i] and rows[i][0][1]<j:heapq.heappop(rows[i])
                    while cols[j] and cols[j][0][1]<i:heapq.heappop(cols[j])
                    d=min(rows[i][0][0] if rows[i] else 10**9,cols[j][0][0] if cols[j] else 10**9)+1
                if d<10**9:
                    heapq.heappush(rows[i],(d,j+grid[i][j]))
                    heapq.heappush(cols[j],(d,i+grid[i][j]))
        return d if d<10**9 else -1
