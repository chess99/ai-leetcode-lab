# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:51Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        distance = [[rows * columns] * columns for _ in range(rows)]
        distance[0][0] = 0
        queue = deque([(0, 0)])
        while queue:
            row, column = queue.popleft()
            for direction, (row_delta, column_delta) in enumerate(directions, 1):
                next_row, next_column = row + row_delta, column + column_delta
                if not (0 <= next_row < rows and 0 <= next_column < columns):
                    continue
                cost = direction != grid[row][column]
                candidate = distance[row][column] + cost
                if candidate < distance[next_row][next_column]:
                    distance[next_row][next_column] = candidate
                    if cost:
                        queue.append((next_row, next_column))
                    else:
                        queue.appendleft((next_row, next_column))
        return distance[-1][-1]
