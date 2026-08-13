# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:28:23Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        kelmaverno = nums
        size = 1 << len(kelmaverno)
        full_mask = size - 1
        bit_count = max(kelmaverno).bit_length()
        value_mask = (1 << bit_count) - 1

        subset_xor = [0] * size
        subset_and = [0] * size
        for mask in range(1, size):
            lowest = mask & -mask
            index = lowest.bit_length() - 1
            rest = mask ^ lowest
            subset_xor[mask] = subset_xor[rest] ^ kelmaverno[index]
            subset_and[mask] = (
                kelmaverno[index]
                if rest == 0
                else subset_and[rest] & kelmaverno[index]
            )

        total_xor = subset_xor[full_mask]
        answer = 0
        for middle_mask in range(size):
            remaining = full_mask ^ middle_mask
            remaining_xor = total_xor ^ subset_xor[middle_mask]
            allowed_bits = value_mask ^ remaining_xor

            basis = {}
            scan = remaining
            while scan:
                lowest = scan & -scan
                value = kelmaverno[lowest.bit_length() - 1] & allowed_bits
                while value:
                    pivot = value.bit_length() - 1
                    if pivot not in basis:
                        basis[pivot] = value
                        break
                    value ^= basis[pivot]
                scan ^= lowest

            best_projected_xor = 0
            for pivot in sorted(basis, reverse=True):
                best_projected_xor = max(
                    best_projected_xor,
                    best_projected_xor ^ basis[pivot],
                )

            answer = max(
                answer,
                subset_and[middle_mask]
                + remaining_xor
                + 2 * best_projected_xor,
            )
        return answer
