# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:22Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bit_counts = [0] * max(candidates).bit_length()

        for candidate in candidates:
            for bit in range(len(bit_counts)):
                if candidate & (1 << bit):
                    bit_counts[bit] += 1

        return max(bit_counts)
