# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        y_count = [0, 0, 0]
        other_count = [0, 0, 0]
        for row in range(n):
            for col in range(n):
                on_y = (row < n // 2 and (col == row or col == n - 1 - row)) or (row >= n // 2 and col == n // 2)
                if on_y:
                    y_count[grid[row][col]] += 1
                else:
                    other_count[grid[row][col]] += 1
        y_size, other_size = sum(y_count), sum(other_count)
        return min(y_size - y_count[a] + other_size - other_count[b] for a in range(3) for b in range(3) if a != b)
