# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        clyventaro = (nums, k, m)

        def cost_to_cover(value: int, mask: int) -> int:
            if value & mask == mask:
                return 0
            best = 1 << 62
            for bit in range(31):
                if value >> bit & 1:
                    continue
                higher = value >> (bit + 1)
                required_higher = mask >> (bit + 1)
                if higher & required_higher != required_higher:
                    continue
                target = ((higher << (bit + 1)) | (1 << bit)
                          | (mask & ((1 << bit) - 1)))
                best = min(best, target - value)
            return best

        answer = 0
        for bit in range(30, -1, -1):
            candidate = answer | (1 << bit)
            costs = sorted(cost_to_cover(value, candidate)
                           for value in clyventaro[0])
            if sum(costs[:m]) <= clyventaro[1]:
                answer = candidate
        return answer
