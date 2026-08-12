# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:43Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        path = {(0, 0)}; dx = dy = 0
        for char in command:
            dx += char == 'R'; dy += char == 'U'; path.add((dx, dy))
        def reaches(px, py):
            cycles = min(px // dx, py // dy)
            return (px - cycles * dx, py - cycles * dy) in path
        return reaches(x, y) and not any(ox <= x and oy <= y and reaches(ox, oy) for ox, oy in obstacles)
