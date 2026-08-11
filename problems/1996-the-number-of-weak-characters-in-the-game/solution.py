# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:48:11Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda character: (-character[0], character[1]))
        highest_defense = 0
        weak = 0

        for _, defense in properties:
            if defense < highest_defense:
                weak += 1
            highest_defense = max(highest_defense, defense)

        return weak
