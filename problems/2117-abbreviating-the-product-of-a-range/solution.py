# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:09Z
# Experiment: ai-leetcode-lab, round 1
import math


class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        modulus = 10 ** 10
        suffix = 1
        count_two = 0
        count_five = 0

        for value in range(left, right + 1):
            current = value
            while current % 2 == 0:
                current //= 2
                count_two += 1
            while current % 5 == 0:
                current //= 5
                count_five += 1
            suffix = suffix * current % modulus

        zeros = min(count_two, count_five)
        suffix = suffix * pow(2, count_two - zeros, modulus) % modulus
        suffix = suffix * pow(5, count_five - zeros, modulus) % modulus

        logarithm = math.fsum(math.log10(value)
                              for value in range(left, right + 1)) - zeros
        exponent = math.floor(logarithm + 1e-12)
        digits = exponent + 1
        if digits <= 10:
            return f"{suffix}e{zeros}"

        leading = int(10 ** (logarithm - exponent + 4))
        leading = min(leading, 99999)
        return f"{leading}...{suffix % 100000:05d}e{zeros}"
