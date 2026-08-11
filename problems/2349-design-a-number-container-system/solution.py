# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:21:29Z
# Experiment: ai-leetcode-lab, round 1

from collections import defaultdict
from heapq import heappop, heappush


class NumberContainers:
    def __init__(self):
        self.index_to_number = {}
        self.number_to_indices = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        if self.index_to_number.get(index) == number:
            return
        self.index_to_number[index] = number
        heappush(self.number_to_indices[number], index)

    def find(self, number: int) -> int:
        heap = self.number_to_indices[number]
        while heap and self.index_to_number.get(heap[0]) != number:
            heappop(heap)
        return heap[0] if heap else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index, number)
# param_2 = obj.find(number)
