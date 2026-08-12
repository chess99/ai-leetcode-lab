# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:45Z
# Experiment: ai-leetcode-lab, round 1
from math import comb


class Solution:
    def keyboard(self, k: int, n: int) -> int:
        mod = 1_000_000_007
        ways = [0] * (n + 1)
        ways[0] = 1
        for _ in range(26):
            next_ways = [0] * (n + 1)
            for length, current in enumerate(ways):
                if not current:
                    continue
                for count in range(min(k, n - length) + 1):
                    next_ways[length + count] += current * comb(length + count, count)
                    next_ways[length + count] %= mod
            ways = next_ways
        return ways[n]
