# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:43:08Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def visit(node, left, right):
            nonlocal answer
            if not node: return
            answer = max(answer, left, right)
            visit(node.left, right + 1, 0)
            visit(node.right, 0, left + 1)
        visit(root, 0, 0)
        return answer
