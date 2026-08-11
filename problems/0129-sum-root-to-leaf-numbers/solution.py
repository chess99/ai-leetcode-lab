# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:24:46Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional


class Solution:
    def sumNumbers(self, root: Optional["TreeNode"]) -> int:
        def dfs(node: Optional["TreeNode"], number: int) -> int:
            if not node:
                return 0
            number = number * 10 + node.val
            if not node.left and not node.right:
                return number
            return dfs(node.left, number) + dfs(node.right, number)

        return dfs(root, 0)
