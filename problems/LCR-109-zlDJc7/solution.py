# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:27Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        blocked = set(deadends)
        if '0000' in blocked:
            return -1
        queue = deque([('0000', 0)])
        visited = {'0000'}
        while queue:
            state, steps = queue.popleft()
            if state == target:
                return steps
            for index in range(4):
                digit = int(state[index])
                for change in (-1, 1):
                    neighbor = state[:index] + str((digit + change) % 10) + state[index + 1:]
                    if neighbor not in blocked and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, steps + 1))
        return -1
