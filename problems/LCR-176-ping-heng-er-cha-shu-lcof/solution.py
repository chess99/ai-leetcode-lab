# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:46:45Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            if left < 0 or right < 0 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return height(root) >= 0
