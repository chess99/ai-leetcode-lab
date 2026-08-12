# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:19Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def extractMantra(self, matrix: List[str], mantra: str) -> int:
        rows, columns = len(matrix), len(matrix[0])
        infinity = 10 ** 9
        distance = [[infinity] * columns for _ in range(rows)]
        distance[0][0] = 0
        for target in mantra:
            # 二维曼哈顿距离变换：正反两次扫描传播四个方向的最短移动代价。
            for row in range(rows):
                for column in range(columns):
                    if row:
                        distance[row][column] = min(distance[row][column], distance[row - 1][column] + 1)
                    if column:
                        distance[row][column] = min(distance[row][column], distance[row][column - 1] + 1)
            for row in range(rows - 1, -1, -1):
                for column in range(columns - 1, -1, -1):
                    if row + 1 < rows:
                        distance[row][column] = min(distance[row][column], distance[row + 1][column] + 1)
                    if column + 1 < columns:
                        distance[row][column] = min(distance[row][column], distance[row][column + 1] + 1)

            next_distance = [[infinity] * columns for _ in range(rows)]
            found = False
            for row in range(rows):
                for column in range(columns):
                    if matrix[row][column] == target:
                        next_distance[row][column] = distance[row][column] + 1
                        found = True
            if not found:
                return -1
            distance = next_distance
        return min(map(min, distance))
