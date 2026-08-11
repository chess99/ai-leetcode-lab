# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:55:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid); zeros = [next((i for i, value in enumerate(reversed(row)) if value), n) for row in grid]; swaps = 0
        for row in range(n):
            candidate = next((i for i in range(row, n) if zeros[i] >= n - row - 1), n)
            if candidate == n: return -1
            swaps += candidate - row; zeros[row:candidate + 1] = [zeros[candidate]] + zeros[row:candidate]
        return swaps
