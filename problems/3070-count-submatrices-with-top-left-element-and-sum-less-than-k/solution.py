# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        answer = 0
        for row in range(rows):
            for col in range(cols):
                prefix[row + 1][col + 1] = grid[row][col] + prefix[row][col + 1] + prefix[row + 1][col] - prefix[row][col]
                if prefix[row + 1][col + 1] <= k:
                    answer += 1
        return answer
