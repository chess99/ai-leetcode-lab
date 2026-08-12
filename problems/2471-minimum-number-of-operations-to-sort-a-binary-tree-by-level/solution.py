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
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def swaps_to_sort(values) -> int:
            target_index = {
                value: index for index, value in enumerate(sorted(values))
            }
            permutation = [target_index[value] for value in values]
            visited = [False] * len(values)
            swaps = 0

            for start in range(len(values)):
                if visited[start]:
                    continue

                cycle_length = 0
                index = start
                while not visited[index]:
                    visited[index] = True
                    cycle_length += 1
                    index = permutation[index]

                swaps += cycle_length - 1

            return swaps

        operations = 0
        queue = deque([root])

        while queue:
            level_values = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level_values.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            operations += swaps_to_sort(level_values)

        return operations
