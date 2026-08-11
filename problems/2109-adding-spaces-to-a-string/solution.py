# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:24Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        pieces = []
        previous = 0
        for position in spaces:
            pieces.append(s[previous:position])
            pieces.append(' ')
            previous = position
        pieces.append(s[previous:])
        return ''.join(pieces)
