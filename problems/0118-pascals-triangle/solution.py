# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:18:58Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row_index in range(numRows):
            row = [1] * (row_index + 1)
            for col in range(1, row_index):
                row[col] = triangle[-1][col - 1] + triangle[-1][col]
            triangle.append(row)
        return triangle
