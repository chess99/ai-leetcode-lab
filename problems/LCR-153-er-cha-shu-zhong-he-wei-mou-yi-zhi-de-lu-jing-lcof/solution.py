# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:35Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations

from typing import List, Optional
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathTarget(self, root: Optional[TreeNode], target: int) -> List[List[int]]:
        if not root:
            return []
        answer, path = [], []
        stack = [(root, 0, False)]
        while stack:
            node, total, exiting = stack.pop()
            if exiting:
                path.pop()
                continue
            path.append(node.val)
            total += node.val
            if not node.left and not node.right and total == target:
                answer.append(path[:])
            stack.append((node, total, True))
            if node.right:
                stack.append((node.right, total, False))
            if node.left:
                stack.append((node.left, total, False))
        return answer
