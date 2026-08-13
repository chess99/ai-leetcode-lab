# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:27:25Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        from bisect import bisect_right

        drinks.sort()
        return sum(bisect_right(drinks, x - price) for price in staple) % 1_000_000_007
