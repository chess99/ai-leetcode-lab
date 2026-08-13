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
        if root is None:
            return 0
        states = {}
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if not visited:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
                continue
            left = states.get(node.left, (0, 0))
            right = states.get(node.right, (0, 0))
            take = node.val + left[1] + right[1]
            skip = max(left) + max(right)
            states[node] = (take, skip)
        return max(states[root])
