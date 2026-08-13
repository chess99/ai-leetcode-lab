# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:48:18Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
from typing import Optional
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return None
        root.left = self.pruneTree(root.left); root.right = self.pruneTree(root.right)
        return root if root.val or root.left or root.right else None
