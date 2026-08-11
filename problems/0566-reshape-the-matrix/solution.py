# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:45:33Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, columns = len(mat), len(mat[0])
        if rows * columns != r * c:
            return mat
        return [[mat[(i * c + j) // columns][(i * c + j) % columns]
                 for j in range(c)] for i in range(r)]
