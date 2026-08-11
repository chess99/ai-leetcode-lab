# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:09Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        reach = added = i = 0
        coins.sort()
        while reach < target:
            if i < len(coins) and coins[i] <= reach + 1:
                reach += coins[i]; i += 1
            else:
                reach += reach + 1; added += 1
        return added
