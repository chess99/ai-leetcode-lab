# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:21Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def getMaximumNumber(self, moles: List[List[int]]) -> int:
        at = {}
        for t, x, y in moles:
            at.setdefault(t, []).append((x, y))
        dp = [[-10**9] * 3 for _ in range(3)]
        dp[1][1] = 0
        last = 0
        for t in sorted(at):
            # The greatest Manhattan distance on a 3x3 board is four.  After
            # four idle seconds every cell can inherit the previous optimum,
            # so larger gaps need no additional simulation.
            for _ in range(min(t - last, 4)):
                nd = [[-10**9] * 3 for _ in range(3)]
                for x in range(3):
                    for y in range(3):
                        for dx, dy in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
                            a, b = x + dx, y + dy
                            if 0 <= a < 3 and 0 <= b < 3:
                                nd[a][b] = max(nd[a][b], dp[x][y])
                dp = nd
            for x, y in at[t]:
                dp[x][y] += 1
            last = t
        return max(map(max, dp))
