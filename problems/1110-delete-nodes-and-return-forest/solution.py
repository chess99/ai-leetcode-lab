# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:21:13Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
from typing import List, Optional


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        removed = set(to_delete)
        forest = []

        def visit(node: Optional[TreeNode], is_root: bool) -> Optional[TreeNode]:
            if not node:
                return None
            deleted = node.val in removed
            if is_root and not deleted:
                forest.append(node)
            node.left = visit(node.left, deleted)
            node.right = visit(node.right, deleted)
            return None if deleted else node

        visit(root, True)
        return forest
