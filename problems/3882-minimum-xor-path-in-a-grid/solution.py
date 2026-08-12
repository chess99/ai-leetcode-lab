# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:43Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        molqaviren = grid
        states = [set() for _ in grid[0]]
        states[0].add(0)
        for row in grid:
            left = set()
            for j, value in enumerate(row):
                states[j] |= left
                states[j] = {xor_value ^ value for xor_value in states[j]}
                left = states[j]
        return min(states[-1])
