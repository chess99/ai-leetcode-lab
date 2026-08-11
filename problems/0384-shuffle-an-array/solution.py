# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:50:42Z
# Experiment: ai-leetcode-lab, round 1
import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.original = nums[:]

    def reset(self) -> List[int]:
        return self.original[:]

    def shuffle(self) -> List[int]:
        shuffled = self.original[:]
        for index in range(len(shuffled) - 1, 0, -1):
            other = random.randrange(index + 1)
            shuffled[index], shuffled[other] = shuffled[other], shuffled[index]
        return shuffled
