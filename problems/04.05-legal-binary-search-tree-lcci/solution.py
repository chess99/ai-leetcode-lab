# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:51Z
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
        current = root
        previous = None
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if previous is not None and current.val <= previous:
                return False
            previous = current.val
            current = current.right
        return True
