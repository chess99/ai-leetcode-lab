# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:14:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        answer = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                top_left = set()
                r, c = row - 1, col - 1
                while r >= 0 and c >= 0:
                    top_left.add(grid[r][c])
                    r -= 1
                    c -= 1
                bottom_right = set()
                r, c = row + 1, col + 1
                while r < rows and c < cols:
                    bottom_right.add(grid[r][c])
                    r += 1
                    c += 1
                answer[row][col] = abs(len(top_left) - len(bottom_right))
        return answer
