# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:56:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = [[rStart, cStart]]
        r, c, steps = rStart, cStart, 1
        while len(result) < rows * cols:
            for dr, dc in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                for _ in range(steps):
                    r += dr; c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                # The arm length increases after every two directions.
                if dr != 0:
                    steps += 1
        return result
