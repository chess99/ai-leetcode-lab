# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:38:06Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float("-inf")
        gains = {}
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if not visited:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
                continue
            left = max(gains.get(node.left, 0), 0)
            right = max(gains.get(node.right, 0), 0)
            best = max(best, node.val + left + right)
            gains[node] = node.val + max(left, right)
        return best
