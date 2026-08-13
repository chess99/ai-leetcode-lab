# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:05:54Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent = None
        node = root
        while node and node.val != key:
            parent = node
            node = node.left if key < node.val else node.right
        if node is None:
            return root
        if node.left and node.right:
            successor_parent = node
            successor = node.right
            while successor.left:
                successor_parent = successor
                successor = successor.left
            node.val = successor.val
            parent, node = successor_parent, successor
        replacement = node.left or node.right
        if parent is None:
            return replacement
        if parent.left is node:
            parent.left = replacement
        else:
            parent.right = replacement
        return root
