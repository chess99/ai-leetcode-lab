# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:11Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        size = len(grid)
        start = (0, 0, 0)
        target = (size - 1, size - 2, 0)
        queue = deque([(start, 0)])
        visited = {start}
        while queue:
            (row, column, vertical), distance = queue.popleft()
            if (row, column, vertical) == target:
                return distance
            following = []
            if not vertical:
                if column + 2 < size and grid[row][column + 2] == 0:
                    following.append((row, column + 1, 0))
                if (row + 1 < size and grid[row + 1][column] == 0 and
                        grid[row + 1][column + 1] == 0):
                    following.append((row + 1, column, 0))
                    following.append((row, column, 1))
            else:
                if row + 2 < size and grid[row + 2][column] == 0:
                    following.append((row + 1, column, 1))
                if (column + 1 < size and grid[row][column + 1] == 0 and
                        grid[row + 1][column + 1] == 0):
                    following.append((row, column + 1, 1))
                    following.append((row, column, 0))
            for state in following:
                if state not in visited:
                    visited.add(state)
                    queue.append((state, distance + 1))
        return -1
