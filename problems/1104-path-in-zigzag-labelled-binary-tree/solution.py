# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:21:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        path = []
        while label:
            path.append(label)
            level = label.bit_length()
            label = (2 ** level - 1 + 2 ** (level - 1) - label) // 2
        return path[::-1]
