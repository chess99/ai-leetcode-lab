# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        top, left = len(grid), len(grid[0])
        bottom = right = -1
        for row, values in enumerate(grid):
            for col, value in enumerate(values):
                if value:
                    top = min(top, row)
                    bottom = max(bottom, row)
                    left = min(left, col)
                    right = max(right, col)
        return (bottom - top + 1) * (right - left + 1)
