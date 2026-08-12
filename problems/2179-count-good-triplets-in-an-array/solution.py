# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T12:52:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def add(self, index):
        index += 1
        while index < len(self.tree):
            self.tree[index] += 1
            index += index & -index

    def prefix_sum(self, end):
        total = 0
        while end:
            total += self.tree[end]
            end -= end & -end
        return total


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        size = len(nums1)
        position = [0] * size
        for index, value in enumerate(nums2):
            position[value] = index
        order = [position[value] for value in nums1]

        left_smaller = [0] * size
        tree = FenwickTree(size)
        for index, value in enumerate(order):
            left_smaller[index] = tree.prefix_sum(value)
            tree.add(value)

        answer = 0
        tree = FenwickTree(size)
        for index in range(size - 1, -1, -1):
            value = order[index]
            right_larger = tree.prefix_sum(size) - tree.prefix_sum(value + 1)
            answer += left_smaller[index] * right_larger
            tree.add(value)
        return answer
