# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:20Z
# Experiment: ai-leetcode-lab, round 1

from collections import deque
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        if start == goal:
            return 0
        queue = deque([start])
        visited = {start}
        steps = 0
        while queue:
            for _ in range(len(queue)):
                value = queue.popleft()
                for number in nums:
                    for next_value in (value + number, value - number, value ^ number):
                        if next_value == goal:
                            return steps + 1
                        if 0 <= next_value <= 1000 and next_value not in visited:
                            visited.add(next_value)
                            queue.append(next_value)
            steps += 1
        return -1
