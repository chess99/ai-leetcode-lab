# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:20Z
# Experiment: ai-leetcode-lab, round 1

from typing import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        EMPTY, GUARD, WALL, GUARDED = 0, 1, 2, 3
        grid = [[EMPTY] * n for _ in range(m)]
        for row, col in guards:
            grid[row][col] = GUARD
        for row, col in walls:
            grid[row][col] = WALL

        for row in range(m):
            visible = False
            for col in range(n):
                if grid[row][col] == WALL:
                    visible = False
                elif grid[row][col] == GUARD:
                    visible = True
                elif visible:
                    grid[row][col] = GUARDED
            visible = False
            for col in range(n - 1, -1, -1):
                if grid[row][col] == WALL:
                    visible = False
                elif grid[row][col] == GUARD:
                    visible = True
                elif visible:
                    grid[row][col] = GUARDED

        for col in range(n):
            visible = False
            for row in range(m):
                if grid[row][col] == WALL:
                    visible = False
                elif grid[row][col] == GUARD:
                    visible = True
                elif visible:
                    grid[row][col] = GUARDED
            visible = False
            for row in range(m - 1, -1, -1):
                if grid[row][col] == WALL:
                    visible = False
                elif grid[row][col] == GUARD:
                    visible = True
                elif visible:
                    grid[row][col] = GUARDED

        return sum(cell == EMPTY for row in grid for cell in row)
