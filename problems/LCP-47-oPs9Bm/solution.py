# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:48Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def securityCheck(self, capacities: List[int], k: int) -> int:
        mod = 1_000_000_007
        ways = [0] * (k + 1)
        ways[0] = 1
        for capacity in capacities:
            contribution = capacity - 1
            next_ways = ways[:]
            for total in range(contribution, k + 1):
                next_ways[total] += ways[total - contribution]
                next_ways[total] %= mod
            ways = next_ways
        return ways[k]
