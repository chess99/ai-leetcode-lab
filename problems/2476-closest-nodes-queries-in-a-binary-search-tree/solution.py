# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:37:21Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from bisect import bisect_left, bisect_right
from typing import List, Optional


class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        values = []
        stack = []
        node = root

        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.left

            node = stack.pop()
            values.append(node.val)
            node = node.right

        answer = []

        for query in queries:
            lower_index = bisect_right(values, query) - 1
            upper_index = bisect_left(values, query)
            lower = values[lower_index] if lower_index >= 0 else -1
            upper = values[upper_index] if upper_index < len(values) else -1
            answer.append([lower, upper])

        return answer
