# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:06:36Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False

        @lru_cache(maxsize=None)
        def can_win(used: int, remaining: int) -> bool:
            for choice in range(1, maxChoosableInteger + 1):
                bit = 1 << (choice - 1)
                if used & bit:
                    continue
                if choice >= remaining or not can_win(used | bit, remaining - choice):
                    return True
            return False

        return can_win(0, desiredTotal)
