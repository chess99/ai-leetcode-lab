# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T12:10:24Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = list(map(sum, mat)); cols = list(map(sum, zip(*mat)))
        return sum(value and rows[i] == cols[j] == 1 for i, row in enumerate(mat) for j, value in enumerate(row))
