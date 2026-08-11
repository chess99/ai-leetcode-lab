# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:01:11Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations
from collections import deque
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        saw_empty = False
        while queue:
            node = queue.popleft()
            if node is None:
                saw_empty = True
                continue
            if saw_empty:
                return False
            queue.append(node.left)
            queue.append(node.right)
        return True
