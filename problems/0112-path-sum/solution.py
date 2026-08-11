# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:18:28Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        stack = [(root, root.val)]
        while stack:
            node, total = stack.pop()
            if node.left is None and node.right is None:
                if total == targetSum:
                    return True
                continue
            if node.left is not None:
                stack.append((node.left, total + node.left.val))
            if node.right is not None:
                stack.append((node.right, total + node.right.val))
        return False
