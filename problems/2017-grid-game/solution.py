# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top_remaining = sum(grid[0])
        bottom_collected = 0
        answer = float("inf")

        for column in range(len(grid[0])):
            top_remaining -= grid[0][column]
            answer = min(answer, max(top_remaining, bottom_collected))
            bottom_collected += grid[1][column]
        return answer
