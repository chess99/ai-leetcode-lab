# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:01:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}
        day = 0
        while n:
            state = tuple(cells)
            if state in seen:
                n %= day - seen[state]
            seen[state] = day
            if n == 0:
                break
            cells = [0] + [int(cells[index - 1] == cells[index + 1]) for index in range(1, 7)] + [0]
            day += 1
            n -= 1
        return cells
