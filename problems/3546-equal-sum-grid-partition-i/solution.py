# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum(map(sum, grid))
        if total % 2:
            return False
        target = total // 2
        running = 0
        for row in grid[:-1]:
            running += sum(row)
            if running == target:
                return True
        running = 0
        columns = len(grid[0])
        for column in range(columns - 1):
            for row in grid:
                running += row[column]
            if running == target:
                return True
        return False
