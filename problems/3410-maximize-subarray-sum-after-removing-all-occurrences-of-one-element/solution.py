# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T15:58:13Z
# Experiment: ai-leetcode-lab, round 1
from typing import List
class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        from collections import defaultdict

        positions = defaultdict(list)
        for index, value in enumerate(nums):
            if value < 0:
                positions[value].append(index)

        size = 1
        while size < len(nums):
            size *= 2
        neg_inf = -10**30
        identity = (0, neg_inf, neg_inf, neg_inf)
        tree = [identity for _ in range(2 * size)]

        def merge(left, right):
            if left[3] == neg_inf:
                return right
            if right[3] == neg_inf:
                return left
            total = left[0] + right[0]
            prefix = max(left[1], left[0] + right[1])
            suffix = max(right[2], right[0] + left[2])
            best = max(left[3], right[3], left[2] + right[1])
            return total, prefix, suffix, best

        def update(index, node):
            index += size
            tree[index] = node
            index //= 2
            while index:
                tree[index] = merge(tree[index * 2], tree[index * 2 + 1])
                index //= 2

        for index, value in enumerate(nums):
            tree[size + index] = (value, value, value, value)
        for index in range(size - 1, 0, -1):
            tree[index] = merge(tree[index * 2], tree[index * 2 + 1])

        answer = tree[1][3]
        for value, indices in positions.items():
            if len(indices) == len(nums):
                continue
            for index in indices:
                update(index, identity)
            answer = max(answer, tree[1][3])
            for index in indices:
                update(index, (value, value, value, value))
        return answer
