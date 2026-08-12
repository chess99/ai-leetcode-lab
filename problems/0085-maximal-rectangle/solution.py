# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:24:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        heights = [0] * len(matrix[0])
        answer = 0
        for row in matrix:
            for column, value in enumerate(row):
                heights[column] = heights[column] + 1 if value == '1' else 0
            stack = []
            for index in range(len(heights) + 1):
                height = heights[index] if index < len(heights) else 0
                start = index
                while stack and stack[-1][1] > height:
                    start, previous_height = stack.pop()
                    answer = max(answer, previous_height * (index - start))
                if not stack or stack[-1][1] < height:
                    stack.append((start, height))
        return answer
