# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:31:04Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        longest = 0
        def dfs(node):
            nonlocal longest
            if node is None: return 0
            left, right = dfs(node.left), dfs(node.right)
            left_path = left + 1 if node.left and node.left.val == node.val else 0
            right_path = right + 1 if node.right and node.right.val == node.val else 0
            longest = max(longest, left_path + right_path)
            return max(left_path, right_path)
        dfs(root); return longest
