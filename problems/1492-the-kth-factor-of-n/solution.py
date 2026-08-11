# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:53:32Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        small_factors = []
        large_factors = []
        factor = 1

        while factor * factor <= n:
            if n % factor == 0:
                small_factors.append(factor)
                paired_factor = n // factor
                if paired_factor != factor:
                    large_factors.append(paired_factor)
            factor += 1

        factors = small_factors + large_factors[::-1]
        if k <= len(factors):
            return factors[k - 1]

        return -1
