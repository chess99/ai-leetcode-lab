# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:24:17Z
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        result = []
        stack = [(root, targetSum - root.val, [root.val])]
        while stack:
            node, remaining, path = stack.pop()
            if node.left is None and node.right is None:
                if remaining == 0:
                    result.append(path)
                continue
            if node.right:
                stack.append((node.right, remaining - node.right.val, path + [node.right.val]))
            if node.left:
                stack.append((node.left, remaining - node.left.val, path + [node.left.val]))
        return result
