# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:14Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(); trainers.sort(); i = j = matched = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]: matched += 1; i += 1
            j += 1
        return matched
