# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:14:03Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left
from random import randint
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sums.append(total)

    def pickIndex(self) -> int:
        target = randint(1, self.prefix_sums[-1])
        return bisect_left(self.prefix_sums, target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
