# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T14:40:43Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1
        counts = [0] * 32
        for value in nums:
            counts[value.bit_length() - 1] += 1
        operations = 0
        for bit in range(31):
            if target >> bit & 1:
                if counts[bit] == 0:
                    higher = bit + 1
                    while counts[higher] == 0:
                        higher += 1
                    while higher > bit:
                        counts[higher] -= 1
                        counts[higher - 1] += 2
                        higher -= 1
                        operations += 1
                counts[bit] -= 1
            counts[bit + 1] += counts[bit] // 2
        return operations
