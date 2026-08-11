# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:53:29Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, columns = len(heights), len(heights[0])

        def reachable(starts):
            seen = set(starts)
            stack = list(starts)
            while stack:
                row, column = stack.pop()
                for next_row, next_column in ((row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)):
                    if (0 <= next_row < rows and 0 <= next_column < columns and
                            (next_row, next_column) not in seen and
                            heights[next_row][next_column] >= heights[row][column]):
                        seen.add((next_row, next_column))
                        stack.append((next_row, next_column))
            return seen

        pacific = reachable([(row, 0) for row in range(rows)] + [(0, column) for column in range(columns)])
        atlantic = reachable([(row, columns - 1) for row in range(rows)] + [(rows - 1, column) for column in range(columns)])
        return [[row, column] for row in range(rows) for column in range(columns) if (row, column) in pacific and (row, column) in atlantic]
