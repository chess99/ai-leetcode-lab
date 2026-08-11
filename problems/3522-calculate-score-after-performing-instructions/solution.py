# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T22:15:53Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        seen = set()
        score = 0
        index = 0
        while 0 <= index < len(instructions) and index not in seen:
            seen.add(index)
            if instructions[index] == 'add':
                score += values[index]
                index += 1
            else:
                index += values[index]
        return score
