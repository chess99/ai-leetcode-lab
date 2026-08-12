# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T08:09:53Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        size = len(stoneValue)
        difference = [0] * (size + 1)
        for index in range(size - 1, -1, -1):
            taken = 0
            difference[index] = -10 ** 9
            for count in range(1, 4):
                if index + count > size:
                    break
                taken += stoneValue[index + count - 1]
                difference[index] = max(
                    difference[index], taken - difference[index + count])
        if difference[0] > 0:
            return 'Alice'
        if difference[0] < 0:
            return 'Bob'
        return 'Tie'
