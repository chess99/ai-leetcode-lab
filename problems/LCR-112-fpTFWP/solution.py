# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:27Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, columns = len(matrix), len(matrix[0])
        outdegree = [[0] * columns for _ in range(rows)]
        queue = deque()
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for row in range(rows):
            for column in range(columns):
                outdegree[row][column] = sum(
                    0 <= row + dr < rows and 0 <= column + dc < columns and
                    matrix[row + dr][column + dc] > matrix[row][column]
                    for dr, dc in directions)
                if outdegree[row][column] == 0:
                    queue.append((row, column))
        length = 0
        while queue:
            length += 1
            for _ in range(len(queue)):
                row, column = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, column + dc
                    if (0 <= nr < rows and 0 <= nc < columns and
                            matrix[nr][nc] < matrix[row][column]):
                        outdegree[nr][nc] -= 1
                        if outdegree[nr][nc] == 0:
                            queue.append((nr, nc))
        return length
