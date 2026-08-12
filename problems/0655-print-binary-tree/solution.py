# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:29:05Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        if root is None:
            return []

        def height(node): return 0 if node is None else 1 + max(height(node.left), height(node.right))
        h = height(root); result = [[""] * (2 ** h - 1) for _ in range(h)]
        def fill(node, row, left, right):
            if node is None: return
            mid = (left + right) // 2; result[row][mid] = str(node.val)
            fill(node.left, row + 1, left, mid - 1); fill(node.right, row + 1, mid + 1, right)
        fill(root, 0, 0, len(result[0]) - 1)
        return result
