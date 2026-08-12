# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T13:47:53Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_right
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        differences = [first - second for first, second in zip(nums1, nums2)]
        coordinates = sorted(set(differences))
        tree = [0] * (len(coordinates) + 1)

        def add(index):
            index += 1
            while index < len(tree):
                tree[index] += 1
                index += index & -index

        def prefix(end):
            total = 0
            while end:
                total += tree[end]
                end -= end & -end
            return total

        answer = 0
        for current in differences:
            answer += prefix(bisect_right(coordinates, current + diff))
            add(bisect_right(coordinates, current) - 1)
        return answer
