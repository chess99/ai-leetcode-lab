# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        champion = 0
        wins = 0
        for challenger in range(1, len(skills)):
            if skills[champion] > skills[challenger]:
                wins += 1
            else:
                champion = challenger
                wins = 1
            if wins >= k:
                return champion
        return champion
