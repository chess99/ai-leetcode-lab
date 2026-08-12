# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:45Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        modulus = 1_000_000_007
        if primeFactors <= 3:
            return primeFactors
        quotient, remainder = divmod(primeFactors, 3)
        if remainder == 0:
            return pow(3, quotient, modulus)
        if remainder == 1:
            return pow(3, quotient - 1, modulus) * 4 % modulus
        return pow(3, quotient, modulus) * 2 % modulus
