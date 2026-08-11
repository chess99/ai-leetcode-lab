# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:14:56Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(); return sum(piles[index] for index in range(len(piles)//3, len(piles), 2))
