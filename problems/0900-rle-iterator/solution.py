# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:56:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.index = 0

    def next(self, n: int) -> int:
        while self.index < len(self.encoding) and n > self.encoding[self.index]:
            n -= self.encoding[self.index]
            self.index += 2
        if self.index == len(self.encoding):
            return -1
        self.encoding[self.index] -= n
        return self.encoding[self.index + 1]


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
