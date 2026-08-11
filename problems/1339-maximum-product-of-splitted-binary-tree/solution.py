# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:41:14Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums = []
        def total(node):
            if not node: return 0
            value = node.val + total(node.left) + total(node.right)
            sums.append(value)
            return value
        whole = total(root)
        return max(value * (whole - value) for value in sums) % (10 ** 9 + 7)
