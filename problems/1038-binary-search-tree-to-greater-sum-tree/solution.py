# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:12:55Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
from typing import Optional


class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0

        def traverse(node: Optional[TreeNode]) -> None:
            nonlocal total
            if not node:
                return
            traverse(node.right)
            total += node.val
            node.val = total
            traverse(node.left)

        traverse(root)
        return root
