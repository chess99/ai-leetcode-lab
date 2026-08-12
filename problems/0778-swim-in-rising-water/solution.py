# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:50Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        size = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        while heap:
            time, row, column = heapq.heappop(heap)
            if row == size - 1 and column == size - 1:
                return time
            for next_row, next_column in ((row-1,column),(row+1,column),
                                          (row,column-1),(row,column+1)):
                if (0 <= next_row < size and 0 <= next_column < size and
                        (next_row, next_column) not in visited):
                    visited.add((next_row, next_column))
                    heapq.heappush(heap, (max(time, grid[next_row][next_column]),
                                          next_row, next_column))
