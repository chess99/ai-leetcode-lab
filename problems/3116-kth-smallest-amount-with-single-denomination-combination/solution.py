# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:15:57Z
# Experiment: ai-leetcode-lab, round 1
from math import gcd
from typing import List


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins = sorted(set(coins))
        coins = [coin for index, coin in enumerate(coins)
                 if all(coin % previous for previous in coins[:index])]

        coefficients = {}
        for coin in coins:
            updates = {coin: 1}
            for multiple, coefficient in list(coefficients.items()):
                combined = multiple // gcd(multiple, coin) * coin
                updates[combined] = updates.get(combined, 0) - coefficient
            for multiple, coefficient in updates.items():
                coefficients[multiple] = coefficients.get(multiple, 0) + coefficient

        def count(limit):
            return sum(coefficient * (limit // multiple)
                       for multiple, coefficient in coefficients.items())

        low = 1
        high = min(coins) * k
        while low < high:
            middle = (low + high) // 2
            if count(middle) >= k:
                high = middle
            else:
                low = middle + 1
        return low
