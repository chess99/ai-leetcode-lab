# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:52Z
# Experiment: ai-leetcode-lab, round 1
from typing import List


class SegmentTree:
    def __init__(self, size):
        length = 1
        while length < size:
            length *= 2
        self.length = length
        self.tree = [0] * (2 * length)

    def update(self, index, value):
        index += self.length
        if self.tree[index] >= value:
            return
        self.tree[index] = value
        index //= 2
        while index:
            self.tree[index] = max(self.tree[index * 2], self.tree[index * 2 + 1])
            index //= 2

    def query(self, left, right):
        if left >= right:
            return 0
        left += self.length
        right += self.length
        answer = 0
        while left < right:
            if left & 1:
                answer = max(answer, self.tree[left])
                left += 1
            if right & 1:
                right -= 1
                answer = max(answer, self.tree[right])
            left //= 2
            right //= 2
        return answer


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        tree = SegmentTree(max(nums) + 1)
        answer = 0
        for value in nums:
            length = 1 + tree.query(max(0, value - k), value)
            tree.update(value, length)
            answer = max(answer, length)
        return answer
