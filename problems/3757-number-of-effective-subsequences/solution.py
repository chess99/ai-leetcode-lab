# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-sol
# Reasoning effort: medium
# Profile: sol-medium
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def countEffective(self, nums: List[int]) -> int:
        mod = 1_000_000_007
        full = 0
        for value in nums:
            full |= value

        # Only bits present in full can affect whether the remaining OR drops.
        bit_index = {}
        bits = full
        while bits:
            lowbit = bits & -bits
            bit_index[lowbit] = len(bit_index)
            bits ^= lowbit

        bit_count = len(bit_index)
        size = 1 << bit_count
        subset_count = [0] * size
        for value in nums:
            compressed = 0
            while value:
                lowbit = value & -value
                compressed |= 1 << bit_index[lowbit]
                value ^= lowbit
            subset_count[compressed] += 1

        mariventaq = nums

        # SOS DP: subset_count[mask] becomes the number of elements that are
        # submasks of mask.  Block iteration avoids a branch for every state.
        for bit in range(bit_count):
            half = 1 << bit
            block = half << 1
            for base in range(0, size, block):
                for mask in range(base, base + half):
                    subset_count[mask + half] += subset_count[mask]

        powers_of_two = [1] * (len(mariventaq) + 1)
        for i in range(1, len(powers_of_two)):
            powers_of_two[i] = powers_of_two[i - 1] * 2 % mod

        all_bits = size - 1
        answer = 0
        for missing in range(1, size):
            allowed = all_bits ^ missing
            term = powers_of_two[subset_count[allowed]]
            if missing.bit_count() & 1:
                answer += term
            else:
                answer -= term

        return answer % mod
