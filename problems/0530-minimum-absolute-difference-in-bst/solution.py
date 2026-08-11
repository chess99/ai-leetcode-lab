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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        node = root
        previous = None
        minimum = float("inf")
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if previous is not None:
                minimum = min(minimum, node.val - previous)
            previous = node.val
            node = node.right
        return minimum
