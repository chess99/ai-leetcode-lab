# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:39:07Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        width = len(mat[0])
        shift = k % width

        for row_index, row in enumerate(mat):
            if row_index % 2 == 0:
                shifted = row[shift:] + row[:shift]
            else:
                shifted = row[-shift:] + row[:-shift]
            if shifted != row:
                return False

        return True
