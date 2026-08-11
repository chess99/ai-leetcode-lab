# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:21:15Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [(root, False)]
        result = {}
        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if not visited:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
                continue

            left_depth, left_lca = result.get(node.left, (0, None))
            right_depth, right_lca = result.get(node.right, (0, None))
            if left_depth == right_depth:
                result[node] = (left_depth + 1, node)
            elif left_depth > right_depth:
                result[node] = (left_depth + 1, left_lca)
            else:
                result[node] = (right_depth + 1, right_lca)
        return result[root][1]
