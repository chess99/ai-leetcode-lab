# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:29:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        while root and (root.val < low or root.val > high):
            root = root.right if root.val < low else root.left

        node = root
        while node:
            while node.left and node.left.val < low:
                node.left = node.left.right
            node = node.left

        node = root
        while node:
            while node.right and node.right.val > high:
                node.right = node.right.left
            node = node.right

        return root
