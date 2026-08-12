# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:59:31Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        rows_by_value = {}
        for row, values in enumerate(grid):
            for value in set(values):
                rows_by_value[value] = rows_by_value.get(value, 0) | 1 << row

        dp = [-1] * (1 << len(grid))
        dp[0] = 0
        for value, available in rows_by_value.items():
            next_dp = dp[:]
            for mask, score in enumerate(dp):
                if score < 0:
                    continue
                choices = available & ~mask
                while choices:
                    bit = choices & -choices
                    next_dp[mask | bit] = max(next_dp[mask | bit], score + value)
                    choices -= bit
            dp = next_dp
        return max(dp)
