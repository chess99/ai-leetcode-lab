# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:45:55Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, sold, rest = float("-inf"), 0, 0
        for price in prices: hold, sold, rest = max(hold, rest - price), hold + price, max(rest, sold)
        return max(sold, rest)
