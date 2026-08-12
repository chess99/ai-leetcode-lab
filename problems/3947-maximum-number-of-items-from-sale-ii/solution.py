# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        zenquarilo = (items, budget)
        n = len(items)
        frequency = [0] * (n + 1)
        for factor, _ in items:
            frequency[factor] += 1

        multiples = [0] * (n + 1)
        for factor in range(1, n + 1):
            multiples[factor] = sum(frequency[value]
                                    for value in range(factor, n + 1, factor))

        cheapest = min(price for _, price in items)
        coupons = sorted((price, multiples[factor] - 1) for factor, price in items)
        cost = doubled = 0
        answer = budget // cheapest
        for price, count in coupons:
            if price >= 2 * cheapest or cost + price > budget:
                break
            take = min(count, (budget - cost) // price)
            cost += take * price
            doubled += take
            answer = max(answer, 2 * doubled + (budget - cost) // cheapest)
        return answer
