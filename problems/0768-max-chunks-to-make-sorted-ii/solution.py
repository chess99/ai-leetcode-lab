# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:02:50Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for value in arr:
            if not stack or value >= stack[-1]:
                stack.append(value)
                continue
            maximum = stack.pop()
            while stack and stack[-1] > value:
                stack.pop()
            stack.append(maximum)
        return len(stack)
