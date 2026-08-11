# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:41:41Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        blocked = set(deadends)
        start = "0000"
        if start in blocked:
            return -1
        queue = deque([(start, 0)])
        seen = {start}

        while queue:
            state, steps = queue.popleft()
            if state == target:
                return steps
            for index, digit in enumerate(state):
                for next_digit in ((int(digit) + 1) % 10, (int(digit) - 1) % 10):
                    neighbor = state[:index] + str(next_digit) + state[index + 1:]
                    if neighbor not in blocked and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, steps + 1))
        return -1
