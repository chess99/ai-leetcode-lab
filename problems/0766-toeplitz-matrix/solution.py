# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:59:00Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(matrix[row][col] == matrix[row - 1][col - 1] for row in range(1, len(matrix)) for col in range(1, len(matrix[0])))
