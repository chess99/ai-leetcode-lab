# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:05:54Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val, self.left, self.right = x, None, None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        values=[];stack=[root]
        while stack:
            node=stack.pop()
            if node: values.append(str(node.val));stack.extend([node.right,node.left])
        return ','.join(values)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:return None
        values=iter(map(int,data.split(',')))
        root=TreeNode(next(values));stack=[root]
        for value in values:
            node=TreeNode(value)
            if value<stack[-1].val:stack[-1].left=node
            else:
                parent=None
                while stack and value>stack[-1].val:parent=stack.pop()
                parent.right=node
            stack.append(node)
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
