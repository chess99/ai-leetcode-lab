# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:24:15Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for previous, current in zip(prices, prices[1:]):
            profit += max(0, current - previous)
        return profit
