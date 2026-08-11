# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:10:48Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = tail = TreeNode(0)
        def inorder(node):
            nonlocal tail
            if node:
                inorder(node.left)
                node.left = None
                tail.right = node
                tail = node
                inorder(node.right)
        inorder(root)
        return dummy.right
