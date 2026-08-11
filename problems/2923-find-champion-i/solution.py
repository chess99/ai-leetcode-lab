# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:31:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        return next(i for i in range(len(grid)) if all(grid[i][j] or i == j for j in range(len(grid))))
