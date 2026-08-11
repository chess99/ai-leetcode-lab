# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:56:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        modulo = 1_000_000_007
        stack = []
        total = 0
        for index, value in enumerate(arr + [0]):
            while stack and arr[stack[-1]] > value:
                middle = stack.pop()
                left = stack[-1] if stack else -1
                total += arr[middle] * (middle - left) * (index - middle)
            stack.append(index)
        return total % modulo
