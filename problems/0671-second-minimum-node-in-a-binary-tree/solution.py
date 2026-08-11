# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:57:02Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        answer = float('inf')
        def dfs(node):
            nonlocal answer
            if not node:
                return
            if root.val < node.val < answer:
                answer = node.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return answer if answer < float('inf') else -1
