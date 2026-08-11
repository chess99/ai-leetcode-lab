# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:07:58Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        return [max(len(str(row[c])) for row in grid) for c in range(len(grid[0]))]
