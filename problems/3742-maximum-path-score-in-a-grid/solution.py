# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:52Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        quantelis = (grid, k)
        m, n = len(grid), len(grid[0])
        budget = min(k, m + n - 1)
        previous = [None] * n
        for i in range(m):
            current = [None] * n
            for j in range(n):
                cost = int(grid[i][j] > 0)
                values = [-1] * (budget + 1)
                if i == 0 and j == 0:
                    values[cost] = grid[i][j]
                else:
                    for source in (previous[j] if i else None, current[j - 1] if j else None):
                        if source is None: continue
                        for used in range(budget - cost + 1):
                            if source[used] >= 0:
                                values[used + cost] = max(values[used + cost], source[used] + grid[i][j])
                current[j] = values
            previous = current
        return max(previous[-1])
