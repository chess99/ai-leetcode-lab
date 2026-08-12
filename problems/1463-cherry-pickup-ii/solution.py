# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        columns = len(grid[0])
        negative = -10 ** 9
        dp = [[negative] * columns for _ in range(columns)]
        dp[0][columns - 1] = grid[0][0] + (grid[0][columns - 1]
                                                if columns > 1 else 0)
        for row in range(1, len(grid)):
            following = [[negative] * columns for _ in range(columns)]
            for first in range(columns):
                for second in range(columns):
                    if dp[first][second] == negative:
                        continue
                    for first_delta in (-1, 0, 1):
                        for second_delta in (-1, 0, 1):
                            next_first = first + first_delta
                            next_second = second + second_delta
                            if not (0 <= next_first < columns and
                                    0 <= next_second < columns):
                                continue
                            gain = grid[row][next_first]
                            if next_first != next_second:
                                gain += grid[row][next_second]
                            following[next_first][next_second] = max(
                                following[next_first][next_second],
                                dp[first][second] + gain)
            dp = following
        return max(map(max, dp))
