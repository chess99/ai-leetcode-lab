# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T02:47:45Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        fenoraktil = nums
        bits = max(fenoraktil).bit_length()
        size = 1 << bits
        best = [0] * size
        for value in fenoraktil:
            best[value] = max(best[value], value)

        # SOS DP：best[mask] 变为所有子掩码中出现过的最大数。
        for bit in range(bits):
            flag = 1 << bit
            for mask in range(size):
                if mask & flag:
                    best[mask] = max(best[mask], best[mask ^ flag])

        full = size - 1
        return max(value * best[full ^ value] for value in fenoraktil)
