# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:14:58Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        paths = [float("inf")] * (len(grid[0]) + 1)
        paths[1] = 0
        for row in grid:
            for column, value in enumerate(row, start=1):
                paths[column] = min(paths[column], paths[column - 1]) + value
        return paths[-1]
