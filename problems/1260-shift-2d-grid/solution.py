# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:45:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, columns = len(grid), len(grid[0])
        shift = k % (rows * columns)
        return [[grid[((row * columns + column - shift) % (rows * columns)) // columns]
                 [((row * columns + column - shift) % (rows * columns)) % columns]
                 for column in range(columns)] for row in range(rows)]
