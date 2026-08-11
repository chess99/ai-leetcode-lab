# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:59:43Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        traversal = []
        for row, values in enumerate(grid):
            traversal.extend(values if row % 2 == 0 else reversed(values))
        return traversal[::2]
