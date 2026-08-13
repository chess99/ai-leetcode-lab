# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:59:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        original = image[sr][sc]
        if original == newColor:
            return image
        stack = [(sr, sc)]
        while stack:
            row, column = stack.pop()
            if not (0 <= row < len(image) and 0 <= column < len(image[0])) or image[row][column] != original:
                continue
            image[row][column] = newColor
            stack.extend(((row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)))
        return image
