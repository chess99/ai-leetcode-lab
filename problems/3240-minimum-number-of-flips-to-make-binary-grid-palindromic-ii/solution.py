# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        answer = 0
        for row in range(rows // 2):
            for col in range(cols // 2):
                ones = grid[row][col] + grid[row][cols - 1 - col] + grid[rows - 1 - row][col] + grid[rows - 1 - row][cols - 1 - col]
                answer += min(ones, 4 - ones)

        middle_ones = mismatches = 0
        if rows % 2:
            row = rows // 2
            for col in range(cols // 2):
                pair = grid[row][col] + grid[row][cols - 1 - col]
                if pair == 1:
                    mismatches += 1
                else:
                    middle_ones += pair
        if cols % 2:
            col = cols // 2
            for row in range(rows // 2):
                pair = grid[row][col] + grid[rows - 1 - row][col]
                if pair == 1:
                    mismatches += 1
                else:
                    middle_ones += pair
        if rows % 2 and cols % 2:
            answer += grid[rows // 2][cols // 2]
        answer += mismatches
        if mismatches == 0:
            answer += middle_ones % 4
        return answer
