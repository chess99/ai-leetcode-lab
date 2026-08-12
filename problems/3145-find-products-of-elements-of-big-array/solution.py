# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:59Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        def bit_statistics(limit):
            count = 0
            exponent_sum = 0
            bit = 0
            while 1 << bit <= limit:
                half = 1 << bit
                period = half << 1
                full_periods, remainder = divmod(limit + 1, period)
                ones = full_periods * half + max(0, remainder - half)
                count += ones
                exponent_sum += ones * bit
                bit += 1
            return count, exponent_sum

        def prefix_exponent(length):
            if length == 0:
                return 0

            low, high = 0, 1
            while bit_statistics(high)[0] <= length:
                high <<= 1
            while low + 1 < high:
                middle = (low + high) // 2
                if bit_statistics(middle)[0] <= length:
                    low = middle
                else:
                    high = middle

            used, exponent_sum = bit_statistics(low)
            remaining = length - used
            value = low + 1
            bit = 0
            while remaining:
                if value >> bit & 1:
                    exponent_sum += bit
                    remaining -= 1
                bit += 1
            return exponent_sum

        answer = []
        for left, right, modulus in queries:
            exponent = prefix_exponent(right + 1) - prefix_exponent(left)
            answer.append(pow(2, exponent, modulus))
        return answer
