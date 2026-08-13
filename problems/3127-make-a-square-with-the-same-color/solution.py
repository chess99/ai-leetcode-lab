# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:45:04Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for row in range(2):
            for column in range(2):
                cells = [
                    grid[row][column],
                    grid[row + 1][column],
                    grid[row][column + 1],
                    grid[row + 1][column + 1],
                ]
                if cells.count("B") >= 3 or cells.count("W") >= 3:
                    return True
        return False
