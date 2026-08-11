# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:22Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        start_row, start_col = startPos
        home_row, home_col = homePos
        cost = 0

        row_step = 1 if start_row < home_row else -1
        for row in range(start_row + row_step, home_row + row_step, row_step):
            cost += rowCosts[row]

        col_step = 1 if start_col < home_col else -1
        for col in range(start_col + col_step, home_col + col_step, col_step):
            cost += colCosts[col]

        return cost
