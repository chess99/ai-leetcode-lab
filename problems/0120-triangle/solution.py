# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:24:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        paths = triangle[-1].copy()
        for row in range(len(triangle) - 2, -1, -1):
            for column, value in enumerate(triangle[row]):
                paths[column] = value + min(paths[column], paths[column + 1])
        return paths[0]
