# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:43Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def domino(self, n: int, m: int, broken: List[List[int]]) -> int:
        blocked = {tuple(cell) for cell in broken}
        match = {}

        def augment(row, column, seen):
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = row + dr, column + dc
                if not (0 <= nr < n and 0 <= nc < m) or (nr, nc) in blocked:
                    continue
                if (nr, nc) in seen:
                    continue
                seen.add((nr, nc))
                if (nr, nc) not in match or augment(*match[(nr, nc)], seen):
                    match[(nr, nc)] = (row, column)
                    return True
            return False

        answer = 0
        for row in range(n):
            for column in range(m):
                if (row, column) not in blocked and (row + column) % 2 == 0:
                    answer += augment(row, column, set())
        return answer
