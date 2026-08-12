# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:10Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        mod = 1_000_000_007
        cells = m * n
        factorial = [1] * (cells + 1)
        for value in range(1, cells + 1):
            factorial[value] = factorial[value - 1] * value % mod

        def combination(total: int, choose: int) -> int:
            if choose < 0 or choose > total:
                return 0
            denominator = factorial[choose] * factorial[total - choose] % mod
            return factorial[total] * pow(denominator, mod - 2, mod) % mod

        def line_distance(length: int) -> int:
            return length * (length - 1) * (length + 1) // 6

        pair_sum = (
            n * n * line_distance(m) + m * m * line_distance(n)
        ) % mod
        return pair_sum * combination(cells - 2, k - 2) % mod
