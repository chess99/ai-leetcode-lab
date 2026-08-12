# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:57:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        horizontal_pieces = vertical_pieces = 1
        h = v = 0
        answer = 0

        while h < len(horizontalCut) or v < len(verticalCut):
            if v == len(verticalCut) or (
                h < len(horizontalCut) and horizontalCut[h] >= verticalCut[v]
            ):
                answer += horizontalCut[h] * vertical_pieces
                horizontal_pieces += 1
                h += 1
            else:
                answer += verticalCut[v] * horizontal_pieces
                vertical_pieces += 1
                v += 1

        return answer
