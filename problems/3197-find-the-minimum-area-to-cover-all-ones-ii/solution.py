# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:57:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        inf = rows * cols + 1

        def area(top: int, bottom: int, left: int, right: int) -> int:
            min_row, max_row = rows, -1
            min_col, max_col = cols, -1
            for r in range(top, bottom + 1):
                for c in range(left, right + 1):
                    if grid[r][c]:
                        min_row = min(min_row, r)
                        max_row = max(max_row, r)
                        min_col = min(min_col, c)
                        max_col = max(max_col, c)
            if max_row < 0:
                return inf
            return (max_row - min_row + 1) * (max_col - min_col + 1)

        answer = inf * 3

        for first in range(rows - 2):
            for second in range(first + 1, rows - 1):
                answer = min(
                    answer,
                    area(0, first, 0, cols - 1)
                    + area(first + 1, second, 0, cols - 1)
                    + area(second + 1, rows - 1, 0, cols - 1),
                )

        for first in range(cols - 2):
            for second in range(first + 1, cols - 1):
                answer = min(
                    answer,
                    area(0, rows - 1, 0, first)
                    + area(0, rows - 1, first + 1, second)
                    + area(0, rows - 1, second + 1, cols - 1),
                )

        for r in range(rows - 1):
            for c in range(cols - 1):
                answer = min(
                    answer,
                    area(0, r, 0, cols - 1)
                    + area(r + 1, rows - 1, 0, c)
                    + area(r + 1, rows - 1, c + 1, cols - 1),
                    area(r + 1, rows - 1, 0, cols - 1)
                    + area(0, r, 0, c)
                    + area(0, r, c + 1, cols - 1),
                    area(0, rows - 1, 0, c)
                    + area(0, r, c + 1, cols - 1)
                    + area(r + 1, rows - 1, c + 1, cols - 1),
                    area(0, rows - 1, c + 1, cols - 1)
                    + area(0, r, 0, c)
                    + area(r + 1, rows - 1, 0, c),
                )

        return answer
