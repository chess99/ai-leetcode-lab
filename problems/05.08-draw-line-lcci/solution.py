# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:53Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def drawLine(self, length: int, w: int, x1: int, x2: int, y: int) -> List[int]:
        screen = [0] * length
        integers_per_row = w // 32
        first = y * integers_per_row + x1 // 32
        last = y * integers_per_row + x2 // 32
        for index in range(first, last + 1):
            screen[index] = 0xFFFFFFFF
        screen[first] &= (0xFFFFFFFF >> (x1 % 32))
        screen[last] &= (0xFFFFFFFF << (31 - x2 % 32)) & 0xFFFFFFFF
        for index in range(first, last + 1):
            if screen[index] >= 1 << 31:
                screen[index] -= 1 << 32
        return screen
