# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:28Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def highestRankedKItems(
        self, grid: List[List[int]], pricing: List[int], start: List[int], k: int
    ) -> List[List[int]]:
        rows, columns = len(grid), len(grid[0])
        queue = deque([(start[0], start[1], 0)])
        seen = {tuple(start)}
        candidates = []
        low, high = pricing

        while queue:
            row, column, distance = queue.popleft()
            if low <= grid[row][column] <= high:
                candidates.append((distance, grid[row][column], row, column))
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row, next_column = row + dr, column + dc
                if (
                    0 <= next_row < rows
                    and 0 <= next_column < columns
                    and grid[next_row][next_column] != 0
                    and (next_row, next_column) not in seen
                ):
                    seen.add((next_row, next_column))
                    queue.append((next_row, next_column, distance + 1))

        candidates.sort()
        return [[row, column] for _, _, row, column in candidates[:k]]
