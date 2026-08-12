# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T16:38:19Z
# Experiment: ai-leetcode-lab, round 1
from array import array
from typing import List


class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        prerequisites = [0] * n
        for before, after in edges:
            prerequisites[after] |= 1 << before

        full = (1 << n) - 1
        dp = array('q', [-1]) * (full + 1)
        dp[0] = 0
        for mask in range(full):
            current = dp[mask]
            if current < 0:
                continue
            position = mask.bit_count() + 1
            candidates = full ^ mask
            while candidates:
                bit = candidates & -candidates
                candidates -= bit
                node = bit.bit_length() - 1
                if prerequisites[node] & ~mask:
                    continue
                next_mask = mask | bit
                value = current + position * score[node]
                if value > dp[next_mask]:
                    dp[next_mask] = value
        return dp[full]
