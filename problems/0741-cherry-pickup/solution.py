# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:48Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        size = len(grid)
        negative = -10 ** 9
        dp = [[negative] * size for _ in range(size)]
        dp[0][0] = grid[0][0]
        for steps in range(1, 2 * size - 1):
            following = [[negative] * size for _ in range(size)]
            lower = max(0, steps - size + 1)
            upper = min(size - 1, steps)
            for row1 in range(lower, upper + 1):
                column1 = steps - row1
                if grid[row1][column1] == -1:
                    continue
                for row2 in range(lower, upper + 1):
                    column2 = steps - row2
                    if grid[row2][column2] == -1:
                        continue
                    previous = max(
                        dp[row1][row2],
                        dp[row1 - 1][row2] if row1 else negative,
                        dp[row1][row2 - 1] if row2 else negative,
                        dp[row1 - 1][row2 - 1] if row1 and row2 else negative,
                    )
                    if previous == negative:
                        continue
                    gain = grid[row1][column1]
                    if row1 != row2:
                        gain += grid[row2][column2]
                    following[row1][row2] = previous + gain
            dp = following
        return max(0, dp[size - 1][size - 1])
