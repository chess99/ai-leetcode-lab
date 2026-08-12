# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:25Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[str]) -> int:
        if not matrix:
            return 0
        heights = [0] * len(matrix[0])
        answer = 0
        for row in matrix:
            for column, cell in enumerate(row):
                heights[column] = heights[column] + 1 if cell == '1' else 0
            stack = [-1]
            for index in range(len(heights) + 1):
                current = heights[index] if index < len(heights) else 0
                while stack[-1] != -1 and heights[stack[-1]] > current:
                    height = heights[stack.pop()]
                    answer = max(answer, height * (index - stack[-1] - 1))
                stack.append(index)
        return answer
