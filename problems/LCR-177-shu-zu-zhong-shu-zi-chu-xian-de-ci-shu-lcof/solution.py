# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:44Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def sockCollocation(self, sockets: List[int]) -> List[int]:
        difference = 0
        for color in sockets:
            difference ^= color
        distinguishing_bit = difference & -difference
        first = second = 0
        for color in sockets:
            if color & distinguishing_bit:
                first ^= color
            else:
                second ^= color
        return [first, second]
