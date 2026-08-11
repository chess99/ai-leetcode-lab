# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:29Z
# Experiment: ai-leetcode-lab, round 1

from collections import Counter
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counts = Counter(map(tuple, grid))
        return sum(row_counts[tuple(grid[row][column] for row in range(len(grid)))] for column in range(len(grid)))
