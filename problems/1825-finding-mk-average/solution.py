# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T11:06:47Z
# Experiment: ai-leetcode-lab, round 1
from collections import deque


class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.maximum = 100_000
        self.values = deque()
        self.count_tree = [0] * (self.maximum + 2)
        self.sum_tree = [0] * (self.maximum + 2)

    def _add(self, value, delta):
        index = value
        while index <= self.maximum + 1:
            self.count_tree[index] += delta
            self.sum_tree[index] += delta * value
            index += index & -index

    def _smallest_sum(self, count):
        index = total_count = total_sum = 0
        bit = 1 << 16
        while bit:
            following = index + bit
            if (following < len(self.count_tree) and
                    total_count + self.count_tree[following] <= count):
                index = following
                total_count += self.count_tree[following]
                total_sum += self.sum_tree[following]
            bit >>= 1
        if total_count < count:
            total_sum += (count - total_count) * (index + 1)
        return total_sum

    def addElement(self, num: int) -> None:
        self.values.append(num)
        self._add(num, 1)
        if len(self.values) > self.m:
            self._add(self.values.popleft(), -1)

    def calculateMKAverage(self) -> int:
        if len(self.values) < self.m:
            return -1
        middle_sum = (self._smallest_sum(self.m - self.k) -
                      self._smallest_sum(self.k))
        return middle_sum // (self.m - 2 * self.k)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
