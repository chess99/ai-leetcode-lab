# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:05:26Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [[matrix[row][column] for row in range(len(matrix))]
                for column in range(len(matrix[0]))]
