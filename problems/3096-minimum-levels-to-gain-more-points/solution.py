# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:34:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        total = sum(1 if value else -1 for value in possible)
        prefix = 0
        for index, value in enumerate(possible[:-1], 1):
            prefix += 1 if value else -1
            if prefix > total - prefix:
                return index
        return -1
