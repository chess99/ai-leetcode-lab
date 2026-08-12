# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:51Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countEffective(self, nums: List[int]) -> int:
        mariventaq = nums
        mod = 1_000_000_007
        full = 0
        for value in nums:
            full |= value

        bit_count = full.bit_length()
        size = 1 << bit_count
        subset_count = [0] * size
        for value in nums:
            subset_count[value] += 1

        for bit in range(bit_count):
            step = 1 << bit
            for mask in range(size):
                if mask & step:
                    subset_count[mask] += subset_count[mask ^ step]

        answer = 0
        subset = full
        while subset:
            missing_count = subset_count[full ^ subset]
            term = pow(2, missing_count, mod)
            if subset.bit_count() & 1:
                answer += term
            else:
                answer -= term
            subset = (subset - 1) & full
        return answer % mod
