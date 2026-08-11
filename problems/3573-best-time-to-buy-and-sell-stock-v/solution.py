# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        neg = -10**30
        flat = [neg] * (k + 1); flat[0] = 0
        long = [neg] * (k + 1); short = [neg] * (k + 1)
        for p in prices:
            nf, nl, ns = flat[:], long[:], short[:]
            for t in range(k + 1):
                nl[t] = max(nl[t], flat[t] - p)
                ns[t] = max(ns[t], flat[t] + p)
                if t:
                    nf[t] = max(nf[t], long[t - 1] + p, short[t - 1] - p)
            flat, long, short = nf, nl, ns
        return max(flat)
