# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:45:40Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations


class Solution:
    def findTargetNode(self, root: Optional[TreeNode], cnt: int) -> int:
        stack = []
        node = root
        while True:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            cnt -= 1
            if cnt == 0:
                return node.val
            node = node.left
