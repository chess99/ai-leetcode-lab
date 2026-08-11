# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:25Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        moves = {
            "L": (0, -1),
            "R": (0, 1),
            "U": (-1, 0),
            "D": (1, 0),
        }
        answer = []

        for start in range(len(s)):
            row, col = startPos
            executed = 0

            for index in range(start, len(s)):
                row_delta, col_delta = moves[s[index]]
                next_row = row + row_delta
                next_col = col + col_delta

                if not (0 <= next_row < n and 0 <= next_col < n):
                    break

                row, col = next_row, next_col
                executed += 1

            answer.append(executed)

        return answer
