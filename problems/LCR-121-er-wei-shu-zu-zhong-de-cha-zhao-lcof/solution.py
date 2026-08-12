# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findTargetIn2DPlants(self, plants: List[List[int]], target: int) -> bool:
        if not plants or not plants[0]:
            return False
        row, column = 0, len(plants[0]) - 1
        while row < len(plants) and column >= 0:
            value = plants[row][column]
            if value == target:
                return True
            if value > target:
                column -= 1
            else:
                row += 1
        return False
