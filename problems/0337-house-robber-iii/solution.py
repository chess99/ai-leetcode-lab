# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:47:41Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional, Tuple


class Solution:
    def rob(self, root: Optional["TreeNode"]) -> int:
        def dfs(node: Optional["TreeNode"]) -> Tuple[int, int]:
            if not node:
                return 0, 0
            left, right = dfs(node.left), dfs(node.right)
            take = node.val + left[1] + right[1]
            skip = max(left) + max(right)
            return take, skip

        return max(dfs(root))
