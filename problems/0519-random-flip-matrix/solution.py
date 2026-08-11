# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:13:37Z
# Experiment: ai-leetcode-lab, round 1
from random import randrange
from typing import List


class Solution:

    def __init__(self, m: int, n: int):
        self.columns = n
        self.total = m * n
        self.remaining = self.total
        self.replacements = {}

    def flip(self) -> List[int]:
        index = randrange(self.remaining)
        actual_index = self.replacements.get(index, index)
        self.remaining -= 1
        self.replacements[index] = self.replacements.get(self.remaining, self.remaining)
        return [actual_index // self.columns, actual_index % self.columns]

    def reset(self) -> None:
        self.remaining = self.total
        self.replacements.clear()


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
