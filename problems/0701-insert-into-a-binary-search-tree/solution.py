# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:31:59Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)

        node = root
        while True:
            if val < node.val:
                if node.left is None:
                    node.left = TreeNode(val)
                    break
                node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(val)
                    break
                node = node.right
        return root
