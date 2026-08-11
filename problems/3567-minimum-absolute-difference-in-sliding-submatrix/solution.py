# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = []
        for r in range(m - k + 1):
            row = []
            for c in range(n - k + 1):
                values = sorted({grid[i][j] for i in range(r, r + k) for j in range(c, c + k)})
                row.append(min((b - a for a, b in zip(values, values[1:])), default=0))
            ans.append(row)
        return ans
