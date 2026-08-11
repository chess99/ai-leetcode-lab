# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:59:19Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        finish=[0]*len(skill)
        for power in mana:
            prefix=0; start=0
            for i,ability in enumerate(skill):
                start=max(start,finish[i]-prefix); prefix+=ability*power
            elapsed = 0
            for i, ability in enumerate(skill):
                elapsed += ability * power
                finish[i] = start + elapsed
        return finish[-1]
