# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:36Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        sums = [[0] * cols for _ in range(rows)]
        counts = [[0] * cols for _ in range(rows)]
        for row in range(rows - 2):
            for col in range(cols - 2):
                valid = all(
                    abs(image[r][c] - image[r + dr][c + dc]) <= threshold
                    for r in range(row, row + 3)
                    for c in range(col, col + 3)
                    for dr, dc in ((1, 0), (0, 1))
                    if r + dr < row + 3 and c + dc < col + 3
                )
                if valid:
                    average = sum(image[r][c] for r in range(row, row + 3) for c in range(col, col + 3)) // 9
                    for r in range(row, row + 3):
                        for c in range(col, col + 3):
                            sums[r][c] += average
                            counts[r][c] += 1
        return [
            [sums[r][c] // counts[r][c] if counts[r][c] else image[r][c] for c in range(cols)]
            for r in range(rows)
        ]
