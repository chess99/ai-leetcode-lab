# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:27Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        costs = {char: value for char, value in zip(chars, vals)}
        best = current = 0
        for char in s:
            current = max(0, current + costs.get(char, ord(char) - ord('a') + 1))
            best = max(best, current)
        return best
