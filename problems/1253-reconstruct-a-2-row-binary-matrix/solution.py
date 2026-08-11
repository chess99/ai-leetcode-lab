# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:30:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        top = [0] * len(colsum)
        bottom = [0] * len(colsum)
        for index, value in enumerate(colsum):
            if value == 2:
                top[index] = bottom[index] = 1
                upper -= 1
                lower -= 1
        for index, value in enumerate(colsum):
            if value == 1:
                if upper > lower:
                    top[index] = 1
                    upper -= 1
                else:
                    bottom[index] = 1
                    lower -= 1
        return [top, bottom] if upper == 0 and lower == 0 else []
