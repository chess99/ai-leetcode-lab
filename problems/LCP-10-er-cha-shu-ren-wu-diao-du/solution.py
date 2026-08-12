# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T17:58:44Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minimalExecTime(self, root: TreeNode) -> float:
        def solve(node):
            if node is None:
                return 0.0, 0.0
            left_work, left_time = solve(node.left)
            right_work, right_time = solve(node.right)
            children_work = left_work + right_work
            children_time = max(left_time, right_time, children_work / 2)
            return children_work + node.val, children_time + node.val

        return solve(root)[1]
