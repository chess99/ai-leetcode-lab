# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:58:52Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        return [[max(grid[r+i][c+j] for i in range(3) for j in range(3)) for c in range(n-2)] for r in range(n-2)]
