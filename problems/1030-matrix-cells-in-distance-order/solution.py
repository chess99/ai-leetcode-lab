# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:16:16Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        return sorted([[r,c] for r in range(rows) for c in range(cols)], key=lambda cell: abs(cell[0]-rCenter)+abs(cell[1]-cCenter))
