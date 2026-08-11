# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:42:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.frequency = n
        self.discount = discount
        self.prices = dict(zip(products, prices))
        self.orders = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.orders += 1
        total = sum(self.prices[item] * quantity for item, quantity in zip(product, amount))
        if self.orders % self.frequency == 0:
            total *= (100 - self.discount) / 100
        return total


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
