# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:09Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List


class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.size = 1
        while self.size < len(arr):
            self.size *= 2
        self.tree = [(0, 0)] * (2 * self.size)
        for index, value in enumerate(arr):
            self.tree[self.size + index] = (value, 1)
        for index in range(self.size - 1, 0, -1):
            self.tree[index] = self._merge(self.tree[index * 2],
                                           self.tree[index * 2 + 1])
        self.positions = defaultdict(list)
        for index, value in enumerate(arr):
            self.positions[value].append(index)

    @staticmethod
    def _merge(first, second):
        if first[0] == second[0]:
            return first[0], first[1] + second[1]
        if first[1] >= second[1]:
            return first[0], first[1] - second[1]
        return second[0], second[1] - first[1]

    def query(self, left: int, right: int, threshold: int) -> int:
        query_left, query_right = left, right
        left += self.size
        right += self.size + 1
        left_result = right_result = (0, 0)
        while left < right:
            if left & 1:
                left_result = self._merge(left_result, self.tree[left])
                left += 1
            if right & 1:
                right -= 1
                right_result = self._merge(self.tree[right], right_result)
            left //= 2
            right //= 2
        candidate = self._merge(left_result, right_result)[0]
        indices = self.positions[candidate]
        count = bisect_right(indices, query_right) - bisect_left(indices, query_left)
        return candidate if count >= threshold else -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
