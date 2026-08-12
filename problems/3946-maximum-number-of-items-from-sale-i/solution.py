# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:29Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        valmorendi = (items, budget)
        maximum_factor = max(factor for factor, _ in items)
        frequency = [0] * (maximum_factor + 1)
        for factor, _ in items:
            frequency[factor] += 1

        multiples = [0] * (maximum_factor + 1)
        for factor in range(1, maximum_factor + 1):
            multiples[factor] = sum(frequency[value]
                                    for value in range(factor, maximum_factor + 1, factor))

        dp = [0] * (budget + 1)
        for factor, price in items:
            bonus = multiples[factor] - 1
            next_dp = dp[:]
            for cost in range(price, budget + 1):
                next_dp[cost] = max(next_dp[cost],
                                    dp[cost - price] + bonus + 1,
                                    next_dp[cost - price] + 1)
            dp = next_dp
        return dp[budget]
