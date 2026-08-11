# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:17:50Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(left, right):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            return mirror(left.left, right.right) and mirror(left.right, right.left)

        return not root or mirror(root.left, root.right)
