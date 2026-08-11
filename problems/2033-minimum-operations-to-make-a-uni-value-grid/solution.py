# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        values = [value for row in grid for value in row]
        remainder = values[0] % x
        if any(value % x != remainder for value in values):
            return -1

        values.sort()
        target = values[len(values) // 2]
        return sum(abs(value - target) // x for value in values)
