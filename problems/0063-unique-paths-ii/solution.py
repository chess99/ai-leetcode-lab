# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:14:58Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        columns = len(obstacleGrid[0])
        paths = [0] * columns
        paths[0] = 1
        for row in obstacleGrid:
            for column, cell in enumerate(row):
                if cell == 1:
                    paths[column] = 0
                elif column > 0:
                    paths[column] += paths[column - 1]
        return paths[-1]
