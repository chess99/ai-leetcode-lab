# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:02:09Z
# Experiment: ai-leetcode-lab, round 1
from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced = 0
        for fruit in fruits:
            for index, basket in enumerate(baskets):
                if basket >= fruit:
                    baskets[index] = 0
                    break
            else:
                unplaced += 1
        return unplaced
