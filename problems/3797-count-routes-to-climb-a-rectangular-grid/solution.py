# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:54Z
# Experiment: ai-leetcode-lab, round 1
from math import isqrt
from typing import List


class Solution:
    def numberOfRoutes(self, grid: List[str], d: int) -> int:
        frovitanel = (grid, d)
        rows, columns = len(grid), len(grid[0])
        mod = 1_000_000_007
        vertical_reach = isqrt(d * d - 1)

        def ranged(values: List[int], radius: int, available: str) -> List[int]:
            prefix = [0]
            for value in values:
                prefix.append((prefix[-1] + value) % mod)
            result = [0] * columns
            for column in range(columns):
                if available[column] == '.':
                    left = max(0, column - radius)
                    right = min(columns, column + radius + 1)
                    result[column] = (prefix[right] - prefix[left]) % mod
            return result

        before_horizontal = [int(cell == '.') for cell in grid[-1]]
        for row in range(rows - 1, -1, -1):
            after_horizontal = ranged(before_horizontal, d, grid[row])
            if row == 0:
                return sum(after_horizontal) % mod
            before_horizontal = ranged(after_horizontal, vertical_reach,
                                       grid[row - 1])
        return 0
