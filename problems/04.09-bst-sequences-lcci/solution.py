# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:29Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations

import sys
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def BSTSequences(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return [[]]
        sys.setrecursionlimit(3000)
        answer = []
        path = []

        def search(available) -> None:
            if not available:
                answer.append(path[:])
                return
            for index in range(len(available)):
                node = available[index]
                next_available = available[:index] + available[index + 1 :]
                if node.left is not None:
                    next_available.append(node.left)
                if node.right is not None:
                    next_available.append(node.right)
                path.append(node.val)
                search(next_available)
                path.pop()

        search([root])
        return answer
