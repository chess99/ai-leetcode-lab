# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:39:21Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations

from typing import Optional
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], parent: Optional[TreeNode], grandparent: Optional[TreeNode]) -> int:
            if not node:
                return 0
            value = node.val if grandparent and grandparent.val % 2 == 0 else 0
            return value + dfs(node.left, node, parent) + dfs(node.right, node, parent)

        return dfs(root, None, None)
