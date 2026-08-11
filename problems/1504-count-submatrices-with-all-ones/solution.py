# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:54:20Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        heights = [0] * len(mat[0]); total = 0
        for row in mat:
            for col, value in enumerate(row): heights[col] = heights[col] + 1 if value else 0
            for right in range(len(row)):
                minimum = heights[right]
                for left in range(right, -1, -1):
                    minimum = min(minimum, heights[left]); total += minimum
        return total
