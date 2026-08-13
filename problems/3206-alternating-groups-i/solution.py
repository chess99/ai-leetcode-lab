# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T14:45:50Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        size = len(colors)
        return sum(
            colors[index] != colors[(index + 1) % size]
            and colors[(index + 1) % size] != colors[(index + 2) % size]
            for index in range(size)
        )
