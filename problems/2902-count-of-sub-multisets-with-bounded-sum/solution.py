# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:47Z
# Experiment: ai-leetcode-lab, round 1
from collections import Counter
from typing import List


class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        modulus = 10 ** 9 + 7
        frequencies = Counter(nums)
        dynamic = [0] * (r + 1)
        dynamic[0] = frequencies.pop(0, 0) + 1
        for value, count in frequencies.items():
            updated = [0] * (r + 1)
            for remainder in range(value):
                window = 0
                for total in range(remainder, r + 1, value):
                    window += dynamic[total]
                    expired = total - value * (count + 1)
                    if expired >= 0:
                        window -= dynamic[expired]
                    updated[total] = window % modulus
            dynamic = updated
        return sum(dynamic[l:r + 1]) % modulus
