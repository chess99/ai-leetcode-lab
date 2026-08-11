# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        dug_cells = {tuple(cell) for cell in dig}
        extracted = 0

        for top, left, bottom, right in artifacts:
            if all(
                (row, col) in dug_cells
                for row in range(top, bottom + 1)
                for col in range(left, right + 1)
            ):
                extracted += 1

        return extracted
