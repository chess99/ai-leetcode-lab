# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:58:20Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations

from collections import deque
from typing import Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root; self.candidates = deque(); queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node.left or not node.right: self.candidates.append(node)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

    def insert(self, val: int) -> int:
        parent = self.candidates[0]; node = TreeNode(val)
        if not parent.left: parent.left = node
        else: parent.right = node; self.candidates.popleft()
        self.candidates.append(node); return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
