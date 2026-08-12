# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:49Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache
from typing import List


class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = ((1, 1), (1, -1), (-1, -1), (-1, 1))

        @lru_cache(None)
        def extend(row: int, col: int, direction: int, can_turn: bool) -> int:
            expected = 2 if grid[row][col] in (0, 1) else 0

            def go(next_direction: int, turn: bool) -> int:
                dr, dc = directions[next_direction]
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == expected:
                    return 1 + extend(nr, nc, next_direction, turn)
                return 1

            answer = go(direction, can_turn)
            if can_turn:
                answer = max(answer, go((direction + 1) % 4, False))
            return answer

        answer = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    for direction in range(4):
                        answer = max(answer, extend(row, col, direction, True))
        return answer
