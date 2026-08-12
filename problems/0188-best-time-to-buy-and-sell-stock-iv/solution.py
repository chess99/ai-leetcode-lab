# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:08Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k >= len(prices) // 2: return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))
        buy = [float("-inf")] * k; sell = [0] * k
        for price in prices:
            for i in range(k):
                buy[i] = max(buy[i], (sell[i - 1] if i else 0) - price)
                sell[i] = max(sell[i], buy[i] + price)
        return sell[-1] if sell else 0
