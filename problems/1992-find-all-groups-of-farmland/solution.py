# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, columns = len(land), len(land[0])
        groups = []

        for row in range(rows):
            for column in range(columns):
                if land[row][column] == 0:
                    continue
                if row > 0 and land[row - 1][column] == 1:
                    continue
                if column > 0 and land[row][column - 1] == 1:
                    continue

                bottom, right = row, column
                while bottom + 1 < rows and land[bottom + 1][column] == 1:
                    bottom += 1
                while right + 1 < columns and land[row][right + 1] == 1:
                    right += 1
                groups.append([row, column, bottom, right])

        return groups
