# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:55:39Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner, wins = arr[0], 0
        for challenger in arr[1:]:
            if challenger > winner: winner, wins = challenger, 1
            else: wins += 1
            if wins == k: return winner
        return winner
