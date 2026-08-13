# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:59:24Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        operations = 0
        for column in range(len(grid[0])):
            for row in range(1, len(grid)):
                required = grid[row - 1][column] + 1
                if grid[row][column] < required:
                    operations += required - grid[row][column]
                    grid[row][column] = required
        return operations
