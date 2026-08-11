# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T11:05:44Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaves(root):
            result = []
            def dfs(node):
                if not node:
                    return
                if not node.left and not node.right:
                    result.append(node.val)
                else:
                    dfs(node.left); dfs(node.right)
            dfs(root)
            return result
        return leaves(root1) == leaves(root2)
