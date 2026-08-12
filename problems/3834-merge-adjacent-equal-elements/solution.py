# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:13:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        temarivolo = nums
        stack = []
        for value in temarivolo:
            stack.append(value)
            while len(stack) >= 2 and stack[-1] == stack[-2]:
                merged = stack.pop() * 2
                stack.pop()
                stack.append(merged)
        return stack
