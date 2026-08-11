# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:16:15Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0
        stack = []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            total += node.val
            node.val = total
            node = node.left

        return root
