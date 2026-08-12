# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:59:33Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        index = k - 1
        shift = sum(operations[bit]
                    for bit in range(index.bit_length())
                    if index >> bit & 1)
        return chr(97 + shift % 26)
