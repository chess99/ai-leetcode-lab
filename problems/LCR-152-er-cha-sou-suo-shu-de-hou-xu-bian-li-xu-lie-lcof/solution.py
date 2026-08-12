# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:35Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def verifyTreeOrder(self, postorder: List[int]) -> bool:
        stack = []; upper = float('inf')
        for value in reversed(postorder):
            if value > upper: return False
            while stack and value < stack[-1]: upper = stack.pop()
            stack.append(value)
        return True
