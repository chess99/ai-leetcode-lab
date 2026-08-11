# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:42:49Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = sum(value % 2 for value in position)
        return min(odd, len(position) - odd)
