# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:19:46Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        node = root
        previous = None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if previous is not None and node.val <= previous:
                return False
            previous = node.val
            node = node.right
        return True
