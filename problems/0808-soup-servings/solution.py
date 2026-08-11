# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:46:08Z
# Experiment: ai-leetcode-lab, round 1
from functools import lru_cache


class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1.0
        servings = (n + 24) // 25
        @lru_cache(maxsize=None)
        def probability(a: int, b: int) -> float:
            if a <= 0 and b <= 0: return 0.5
            if a <= 0: return 1.0
            if b <= 0: return 0.0
            return sum(probability(a - da, b - db) for da, db in ((4, 0), (3, 1), (2, 2), (1, 3))) / 4
        return probability(servings, servings)
