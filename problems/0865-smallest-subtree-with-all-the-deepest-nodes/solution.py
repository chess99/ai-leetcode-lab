# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:53:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def find(node):
            if not node: return 0, None
            left_depth, left_node = find(node.left)
            right_depth, right_node = find(node.right)
            if left_depth == right_depth: return left_depth + 1, node
            return (left_depth + 1, left_node) if left_depth > right_depth else (right_depth + 1, right_node)
        return find(root)[1]
