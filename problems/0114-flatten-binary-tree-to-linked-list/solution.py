# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:24:18Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node = root
        while node:
            if node.left:
                predecessor = node.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = node.right
                node.right = node.left
                node.left = None
            node = node.right
