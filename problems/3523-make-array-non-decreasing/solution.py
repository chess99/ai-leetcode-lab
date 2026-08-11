# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:53Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        stack = []
        for value in nums:
            maximum = value
            while stack and stack[-1] > maximum:
                maximum = max(maximum, stack.pop())
            stack.append(maximum)
        return len(stack)
