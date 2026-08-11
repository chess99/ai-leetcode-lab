# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:53:03Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_mins={min(row) for row in matrix}; col_maxes={max(matrix[r][c] for r in range(len(matrix))) for c in range(len(matrix[0]))}
        return list(row_mins & col_maxes)
