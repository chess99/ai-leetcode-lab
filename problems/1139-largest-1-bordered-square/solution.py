# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:23:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        horizontal = [[0] * (cols + 1) for _ in range(rows + 1)]
        vertical = [[0] * (cols + 1) for _ in range(rows + 1)]
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                if grid[row - 1][col - 1]:
                    horizontal[row][col] = horizontal[row][col - 1] + 1
                    vertical[row][col] = vertical[row - 1][col] + 1
        for side in range(min(rows, cols), 0, -1):
            for bottom in range(side, rows + 1):
                for right in range(side, cols + 1):
                    if (horizontal[bottom][right] >= side and vertical[bottom][right] >= side
                            and horizontal[bottom - side + 1][right] >= side
                            and vertical[bottom][right - side + 1] >= side):
                        return side * side
        return 0
