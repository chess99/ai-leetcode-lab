# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:17Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expandBinaryTree(self, root: Optional['TreeNode']) -> Optional['TreeNode']:
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                child = node.left
                node.left = type(node)(-1)
                node.left.left = child
                stack.append(child)
            if node.right:
                child = node.right
                node.right = type(node)(-1)
                node.right.right = child
                stack.append(child)
        return root
