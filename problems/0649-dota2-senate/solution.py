# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:27:17Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        size = len(senate)
        radiant = deque(index for index, party in enumerate(senate) if party == "R")
        dire = deque(index for index, party in enumerate(senate) if party == "D")

        while radiant and dire:
            if radiant[0] < dire[0]:
                radiant.append(radiant.popleft() + size)
                dire.popleft()
            else:
                dire.append(dire.popleft() + size)
                radiant.popleft()

        return "Radiant" if radiant else "Dire"
