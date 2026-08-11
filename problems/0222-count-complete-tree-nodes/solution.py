# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:33:28Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional


class Solution:
    def countNodes(self, root: Optional["TreeNode"]) -> int:
        if not root:
            return 0

        def left_height(node: Optional["TreeNode"]) -> int:
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        left, right = left_height(root.left), left_height(root.right)
        if left == right:
            return (1 << left) + self.countNodes(root.right)
        return (1 << right) + self.countNodes(root.left)
