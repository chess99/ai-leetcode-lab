# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:53Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        modulus = 1_000_000_007
        columns = len(grid[0])
        dynamic = [[0] * k for _ in range(columns)]
        for row, values in enumerate(grid):
            for column, value in enumerate(values):
                current = [0] * k
                remainder = value % k
                if row == 0 and column == 0:
                    current[remainder] = 1
                else:
                    for previous in range(k):
                        count = 0
                        if row:
                            count += dynamic[column][previous]
                        if column:
                            count += dynamic[column - 1][previous]
                        current[(previous + remainder) % k] = count % modulus
                dynamic[column] = current
        return dynamic[-1][0]
