# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:43:09Z
# Experiment: ai-leetcode-lab, round 1
from collections import defaultdict
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved_by_row = defaultdict(int)
        for row, seat in reservedSeats:
            reserved_by_row[row] |= 1 << seat

        left_block = sum(1 << seat for seat in range(2, 6))
        middle_block = sum(1 << seat for seat in range(4, 8))
        right_block = sum(1 << seat for seat in range(6, 10))

        families = 2 * n
        for reserved in reserved_by_row.values():
            left_available = reserved & left_block == 0
            right_available = reserved & right_block == 0

            if left_available and right_available:
                continue
            if left_available or right_available or reserved & middle_block == 0:
                families -= 1
            else:
                families -= 2

        return families
