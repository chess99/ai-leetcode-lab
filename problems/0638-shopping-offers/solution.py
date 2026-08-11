# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:27:16Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache
from typing import List


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        @lru_cache(maxsize=None)
        def minimum_cost(remaining: tuple[int, ...]) -> int:
            best = sum(count * unit_price for count, unit_price in zip(remaining, price))
            for offer in special:
                quantities = offer[:-1]
                if all(quantity <= count for quantity, count in zip(quantities, remaining)):
                    next_remaining = tuple(
                        count - quantity for count, quantity in zip(remaining, quantities)
                    )
                    best = min(best, offer[-1] + minimum_cost(next_remaining))
            return best

        return minimum_cost(tuple(needs))
