# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T03:37:41Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        total = sum(prices)
        for price, discount in zip(prices, discounts):
            total -= price * discount / 100
        return total
