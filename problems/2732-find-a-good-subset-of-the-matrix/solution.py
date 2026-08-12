# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        first = {}
        for index, row in enumerate(grid):
            mask = sum(value << column for column, value in enumerate(row))
            if mask == 0:
                return [index]
            for previous, previous_index in first.items():
                if mask & previous == 0:
                    return sorted([previous_index, index])
            first.setdefault(mask, index)
        return []
