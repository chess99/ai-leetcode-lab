# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:34:30Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        reachable = 0
        for coin in sorted(coins):
            if coin > reachable + 1:
                break
            reachable += coin
        return reachable + 1
