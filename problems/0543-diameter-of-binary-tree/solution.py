# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:45:31Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        heights = {}
        stack = [(root, False)]
        diameter = 0
        while stack:
            node, visited = stack.pop()
            if visited:
                left = heights.get(node.left, 0)
                right = heights.get(node.right, 0)
                diameter = max(diameter, left + right)
                heights[node] = 1 + max(left, right)
            else:
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
                if node.right:
                    stack.append((node.right, False))
        return diameter
