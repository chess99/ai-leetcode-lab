# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:30Z
# Experiment: ai-leetcode-lab, round 1
import heapq
from typing import List


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows = len(grid)
        columns = len(grid[0])
        answer = [0] * len(queries)
        queue = [(grid[0][0], 0, 0)]
        seen = {(0, 0)}
        reached = 0
        for query, query_index in sorted((value, index) for index, value in enumerate(queries)):
            while queue and queue[0][0] < query:
                _, row, column = heapq.heappop(queue)
                reached += 1
                for row_step, column_step in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_row = row + row_step
                    next_column = column + column_step
                    if (0 <= next_row < rows and 0 <= next_column < columns
                            and (next_row, next_column) not in seen):
                        seen.add((next_row, next_column))
                        heapq.heappush(queue, (grid[next_row][next_column], next_row, next_column))
            answer[query_index] = reached
        return answer
