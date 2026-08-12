# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:01:04Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def printKMoves(self, K: int) -> List[str]:
        black = set()
        row = col = direction = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for _ in range(K):
            if (row, col) in black:
                black.remove((row, col))
                direction = (direction - 1) % 4
            else:
                black.add((row, col))
                direction = (direction + 1) % 4
            dr, dc = directions[direction]
            row += dr
            col += dc
        min_row = min([row] + [r for r, _ in black])
        max_row = max([row] + [r for r, _ in black])
        min_col = min([col] + [c for _, c in black])
        max_col = max([col] + [c for _, c in black])
        symbols = "RDLU"
        result = []
        for r in range(min_row, max_row + 1):
            line = []
            for c in range(min_col, max_col + 1):
                if (r, c) == (row, col):
                    line.append(symbols[direction])
                elif (r, c) in black:
                    line.append("X")
                else:
                    line.append("_")
            result.append("".join(line))
        return result
