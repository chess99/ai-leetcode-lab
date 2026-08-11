# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:39:20Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        stack = [start]
        while stack:
            index = stack.pop()
            if arr[index] == 0: return True
            jump = arr[index]; arr[index] = -1
            for next_index in (index - jump, index + jump):
                if 0 <= next_index < len(arr) and arr[next_index] >= 0: stack.append(next_index)
        return False
