# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:10:20Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        size = len(mat)
        total = sum(mat[index][index] + mat[index][size - 1 - index] for index in range(size))
        if size % 2:
            total -= mat[size // 2][size // 2]
        return total
