# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:15:34Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right
from typing import Optional
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def prune(node,total):
            if node is None:return None
            total+=node.val
            if node.left is None and node.right is None:return node if total>=limit else None
            node.left=prune(node.left,total);node.right=prune(node.right,total)
            return node if node.left or node.right else None
        return prune(root,0)
