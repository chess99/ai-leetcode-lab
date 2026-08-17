# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Created: 2026-08-17T09:16:00Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        clyventaro = (nums, k, m)

        def cost_to_cover(value: int, mask: int) -> int:
            missing = mask & ~value
            if missing == 0:
                return 0

            # The highest missing required bit is the first bit at which the
            # smallest valid target must exceed value. Higher bits stay the
            # same; lower required bits are set as cheaply as possible.
            bit = missing.bit_length() - 1
            lower_bits = (1 << bit) - 1
            return ((1 << bit) + (mask & lower_bits)
                    - (value & lower_bits))

        answer = 0
        for bit in range(30, -1, -1):
            candidate = answer | (1 << bit)
            costs = sorted(cost_to_cover(value, candidate)
                           for value in clyventaro[0])
            if sum(costs[:m]) <= clyventaro[1]:
                answer = candidate
        return answer
