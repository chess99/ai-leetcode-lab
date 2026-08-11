# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:46:08Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = [max(row) for row in grid]
        columns = [max(column) for column in zip(*grid)]
        return sum(min(rows[i], columns[j]) - value for i, row in enumerate(grid) for j, value in enumerate(row))
