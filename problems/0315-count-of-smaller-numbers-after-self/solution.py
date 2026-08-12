# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:12Z
# Experiment: ai-leetcode-lab, round 1
from bisect import bisect_left
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ordered = sorted(set(nums))
        tree = [0] * (len(ordered) + 1)

        def query(index):
            total = 0
            while index:
                total += tree[index]
                index -= index & -index
            return total

        answer = []
        for value in reversed(nums):
            rank = bisect_left(ordered, value) + 1
            answer.append(query(rank - 1))
            index = rank
            while index < len(tree):
                tree[index] += 1
                index += index & -index
        return answer[::-1]
