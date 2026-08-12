# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
from collections import deque


class Solution:
    def conveyorBelt(self, matrix: List[str], start: List[int], end: List[int]) -> int:
        rows, columns = len(matrix), len(matrix[0])
        directions = [(-1, 0, '^'), (1, 0, 'v'), (0, -1, '<'), (0, 1, '>')]
        infinity = rows * columns + 1
        distance = [[infinity] * columns for _ in range(rows)]
        distance[start[0]][start[1]] = 0
        queue = deque([(start[0], start[1])])
        while queue:
            row, column = queue.popleft()
            for dr, dc, symbol in directions:
                nr, nc = row + dr, column + dc
                if not (0 <= nr < rows and 0 <= nc < columns):
                    continue
                cost = matrix[row][column] != symbol
                candidate = distance[row][column] + cost
                if candidate >= distance[nr][nc]:
                    continue
                distance[nr][nc] = candidate
                if cost:
                    queue.append((nr, nc))
                else:
                    queue.appendleft((nr, nc))
        return distance[end[0]][end[1]]
