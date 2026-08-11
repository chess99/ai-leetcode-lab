# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:01:24Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def smallestValue(self, n: int) -> int:
        while True:
            x, factor_sum, d = n, 0, 2
            while d * d <= x:
                while x % d == 0:
                    factor_sum += d
                    x //= d
                d += 1
            if x > 1:
                factor_sum += x
            if factor_sum == n:
                return n
            n = factor_sum
