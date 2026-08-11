# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:26Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, columns = len(heights), len(heights[0])
        effort = [[float("inf")] * columns for _ in range(rows)]
        effort[0][0] = 0
        heap = [(0, 0, 0)]

        while heap:
            current_effort, row, column = heapq.heappop(heap)
            if (row, column) == (rows - 1, columns - 1):
                return current_effort
            if current_effort != effort[row][column]:
                continue

            for row_step, column_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row = row + row_step
                next_column = column + column_step
                if not (0 <= next_row < rows and 0 <= next_column < columns):
                    continue

                edge_effort = abs(heights[row][column] - heights[next_row][next_column])
                candidate = max(current_effort, edge_effort)
                if candidate < effort[next_row][next_column]:
                    effort[next_row][next_column] = candidate
                    heapq.heappush(heap, (candidate, next_row, next_column))

        return 0
