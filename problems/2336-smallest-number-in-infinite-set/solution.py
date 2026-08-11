# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:28Z
# Experiment: ai-leetcode-lab, round 1

from heapq import heappop, heappush


class SmallestInfiniteSet:
    def __init__(self):
        self.next_number = 1
        self.added_back = []
        self.added_back_set = set()

    def popSmallest(self) -> int:
        if self.added_back:
            number = heappop(self.added_back)
            self.added_back_set.remove(number)
            return number

        number = self.next_number
        self.next_number += 1
        return number

    def addBack(self, num: int) -> None:
        if num < self.next_number and num not in self.added_back_set:
            heappush(self.added_back, num)
            self.added_back_set.add(num)
