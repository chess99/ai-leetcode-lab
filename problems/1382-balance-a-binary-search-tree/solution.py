# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:43:09Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        stack = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            nodes.append(current)
            current = current.right

        def build_balanced(left: int, right: int) -> TreeNode:
            if left >= right:
                return None

            middle = (left + right) // 2
            node = nodes[middle]
            node.left = build_balanced(left, middle)
            node.right = build_balanced(middle + 1, right)
            return node

        return build_balanced(0, len(nodes))
