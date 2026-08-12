# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0]:
            return []
        rows, columns = len(obstacleGrid), len(obstacleGrid[0])
        stack = [(0, 0, 0)]
        path = []
        failed = set()
        while stack:
            row, column, state = stack.pop()
            if state == 1:
                path.pop()
                failed.add((row, column))
                continue
            if ((row, column) in failed or row >= rows or column >= columns
                    or obstacleGrid[row][column]):
                continue
            path.append([row, column])
            if row == rows - 1 and column == columns - 1:
                return path[:]
            stack.append((row, column, 1))
            stack.append((row + 1, column, 0))
            stack.append((row, column + 1, 0))
        return []
