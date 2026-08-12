# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:03:07Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from typing import Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        paths = 0
        stack = [(root, 0, False)]
        while stack:
            node, prefix_sum, exiting = stack.pop()
            if node is None:
                continue
            if exiting:
                prefix_counts[prefix_sum] -= 1
                continue
            prefix_sum += node.val
            paths += prefix_counts[prefix_sum - targetSum]
            prefix_counts[prefix_sum] += 1
            stack.append((node, prefix_sum, True))
            stack.append((node.right, prefix_sum, False))
            stack.append((node.left, prefix_sum, False))
        return paths
