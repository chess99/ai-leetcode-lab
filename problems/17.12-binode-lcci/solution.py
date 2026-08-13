# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:02:45Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBiNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        current = root
        head = previous = None
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            current.left = None
            if previous:
                previous.right = current
            else:
                head = current
            previous = current
            current = current.right
        return head
