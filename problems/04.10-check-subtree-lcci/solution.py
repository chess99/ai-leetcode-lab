# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:52Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSubTree(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        if not t2:
            return True
        if not t1:
            return False

        def identical(first, second):
            stack = [(first, second)]
            while stack:
                node1, node2 = stack.pop()
                if not node1 or not node2:
                    if node1 is not node2:
                        return False
                    continue
                if node1.val != node2.val:
                    return False
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
            return True

        stack = [t1]
        while stack:
            node = stack.pop()
            if node.val == t2.val and identical(node, t2):
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
