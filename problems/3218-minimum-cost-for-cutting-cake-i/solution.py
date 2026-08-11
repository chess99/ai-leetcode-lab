# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        horizontal_pieces = vertical_pieces = 1
        horizontal_index = vertical_index = 0
        cost = 0
        while horizontal_index < len(horizontalCut) or vertical_index < len(verticalCut):
            if vertical_index == len(verticalCut) or (horizontal_index < len(horizontalCut) and horizontalCut[horizontal_index] >= verticalCut[vertical_index]):
                cost += horizontalCut[horizontal_index] * vertical_pieces
                horizontal_pieces += 1
                horizontal_index += 1
            else:
                cost += verticalCut[vertical_index] * horizontal_pieces
                vertical_pieces += 1
                vertical_index += 1
        return cost
