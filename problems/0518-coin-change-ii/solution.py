# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:13:10Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [0] * (amount + 1)
        ways[0] = 1

        for coin in coins:
            for total in range(coin, amount + 1):
                ways[total] += ways[total - coin]

        return ways[amount]
