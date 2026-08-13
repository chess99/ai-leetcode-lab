# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:37:12Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
from typing import Optional


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        stack = [(root, 0)] if root else []
        while stack:
            node, value = stack.pop()
            node.val = value
            self.values.add(value)
            if node.left: stack.append((node.left, 2 * value + 1))
            if node.right: stack.append((node.right, 2 * value + 2))

    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
