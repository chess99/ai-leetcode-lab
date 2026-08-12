# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:33Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def validateBookSequences(self, putIn: List[int], takeOut: List[int]) -> bool:
        stack = []; index = 0
        for value in putIn:
            stack.append(value)
            while stack and index < len(takeOut) and stack[-1] == takeOut[index]: stack.pop(); index += 1
        return index == len(takeOut)
