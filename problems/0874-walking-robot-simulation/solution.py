# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:53:41Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        blocked = {tuple(obstacle) for obstacle in obstacles}
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        direction = 0
        x = y = 0
        farthest = 0
        for command in commands:
            if command == -1:
                direction = (direction + 1) % 4
            elif command == -2:
                direction = (direction - 1) % 4
            else:
                delta_x, delta_y = directions[direction]
                for _ in range(command):
                    if (x + delta_x, y + delta_y) in blocked:
                        break
                    x += delta_x
                    y += delta_y
                    farthest = max(farthest, x * x + y * y)
        return farthest
