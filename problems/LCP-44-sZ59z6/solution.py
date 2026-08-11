# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:31:48Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def numColor(self, root: TreeNode) -> int:
        colors = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            colors.add(node.val)
            stack.append(node.left)
            stack.append(node.right)
        return len(colors)
