# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        columns = len(matrix[0])
        row_masks = []

        for row in matrix:
            mask = 0
            for column, value in enumerate(row):
                if value == 1:
                    mask |= 1 << column
            row_masks.append(mask)

        maximum = 0

        for selected in range(1 << columns):
            if selected.bit_count() != numSelect:
                continue

            covered = sum(
                (row_mask | selected) == selected
                for row_mask in row_masks
            )
            maximum = max(maximum, covered)

        return maximum
