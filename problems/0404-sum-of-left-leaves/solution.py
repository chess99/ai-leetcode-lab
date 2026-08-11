# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:37:05Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        total = 0
        stack = [(root, False)]
        while stack:
            node, is_left = stack.pop()
            if not node.left and not node.right:
                total += node.val if is_left else 0
            else:
                if node.left:
                    stack.append((node.left, True))
                if node.right:
                    stack.append((node.right, False))
        return total
