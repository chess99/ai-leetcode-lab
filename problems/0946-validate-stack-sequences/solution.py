# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:00:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]; index=0
        for value in pushed:
            stack.append(value)
            while stack and stack[-1]==popped[index]: stack.pop();index+=1
        return not stack
