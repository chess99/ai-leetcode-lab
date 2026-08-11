# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T13:12:34Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        target = set(range(1, len(matrix) + 1))
        return all(set(row) == target for row in matrix) and all(set(col) == target for col in zip(*matrix))
