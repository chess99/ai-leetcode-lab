# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:42:09Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows=[0]*m; cols=[0]*n
        for row,col in indices: rows[row]^=1; cols[col]^=1
        return sum(row^col for row in rows for col in cols)
