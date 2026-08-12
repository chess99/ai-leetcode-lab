# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:41Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        tavolirexu = grid
        banned = 0
        for bit in range(16, -1, -1):
            candidate = banned | (1 << bit)
            if all(any(value & candidate == 0 for value in row) for row in grid):
                banned = candidate
        return ((1 << 17) - 1) ^ banned
