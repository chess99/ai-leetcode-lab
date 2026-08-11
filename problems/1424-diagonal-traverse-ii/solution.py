# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:49:31Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        for row, values in enumerate(nums):
            for col, value in enumerate(values):
                diagonals[row + col].append(value)
        result = []
        for diagonal in range(max(diagonals) + 1):
            result.extend(reversed(diagonals[diagonal]))
        return result
