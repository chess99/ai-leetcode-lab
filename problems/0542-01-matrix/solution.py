# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:16:16Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, columns = len(mat), len(mat[0])
        distances = [[-1] * columns for _ in range(rows)]
        queue = deque()

        for row in range(rows):
            for column in range(columns):
                if mat[row][column] == 0:
                    distances[row][column] = 0
                    queue.append((row, column))

        while queue:
            row, column = queue.popleft()
            for next_row, next_column in ((row - 1, column), (row + 1, column),
                                          (row, column - 1), (row, column + 1)):
                if (0 <= next_row < rows and 0 <= next_column < columns
                        and distances[next_row][next_column] == -1):
                    distances[next_row][next_column] = distances[row][column] + 1
                    queue.append((next_row, next_column))

        return distances
