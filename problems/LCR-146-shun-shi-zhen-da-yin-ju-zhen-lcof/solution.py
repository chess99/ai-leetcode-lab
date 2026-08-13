# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:43:01Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def spiralArray(self, array: List[List[int]]) -> List[int]:
        if not array or not array[0]:
            return []
        top, bottom, left, right = 0, len(array) - 1, 0, len(array[0]) - 1
        result = []
        while top <= bottom and left <= right:
            for column in range(left, right + 1):
                result.append(array[top][column])
            top += 1
            for row in range(top, bottom + 1):
                result.append(array[row][right])
            right -= 1
            if top <= bottom:
                for column in range(right, left - 1, -1):
                    result.append(array[bottom][column])
                bottom -= 1
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(array[row][left])
                left += 1
        return result
