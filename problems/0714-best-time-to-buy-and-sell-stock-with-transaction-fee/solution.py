# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:33:16Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = -prices[0]
        for price in prices[1:]:
            previous_cash = cash
            cash = max(cash, hold + price - fee)
            hold = max(hold, previous_cash - price)
        return cash
