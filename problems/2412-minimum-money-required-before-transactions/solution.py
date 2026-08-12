# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:52Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        losses = sum(max(cost - cashback, 0)
                     for cost, cashback in transactions)
        reserve = max(min(cost, cashback) for cost, cashback in transactions)
        return losses + reserve
