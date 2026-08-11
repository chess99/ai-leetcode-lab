# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:06:48Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        return sum(value > 0 for row in grid for value in row) + sum(map(max, grid)) + sum(map(max, zip(*grid)))
