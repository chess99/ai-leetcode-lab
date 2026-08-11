# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:58:57Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        size = len(grid)
        queue = deque()

        def mark_island(row: int, column: int) -> None:
            stack = [(row, column)]
            grid[row][column] = 2
            while stack:
                current_row, current_column = stack.pop()
                queue.append((current_row, current_column))
                for next_row, next_column in ((current_row - 1, current_column),
                                              (current_row + 1, current_column),
                                              (current_row, current_column - 1),
                                              (current_row, current_column + 1)):
                    if 0 <= next_row < size and 0 <= next_column < size and grid[next_row][next_column] == 1:
                        grid[next_row][next_column] = 2
                        stack.append((next_row, next_column))

        for row in range(size):
            for column in range(size):
                if grid[row][column] == 1:
                    mark_island(row, column)
                    break
            if queue:
                break

        distance = 0
        while queue:
            for _ in range(len(queue)):
                row, column = queue.popleft()
                for next_row, next_column in ((row - 1, column), (row + 1, column),
                                              (row, column - 1), (row, column + 1)):
                    if not (0 <= next_row < size and 0 <= next_column < size):
                        continue
                    if grid[next_row][next_column] == 1:
                        return distance
                    if grid[next_row][next_column] == 0:
                        grid[next_row][next_column] = 2
                        queue.append((next_row, next_column))
            distance += 1
        return -1
