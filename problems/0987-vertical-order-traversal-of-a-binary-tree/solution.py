# AI solution attribution
from typing import List, Optional
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:05Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional["TreeNode"]) -> List[List[int]]:
        nodes = []
        stack = [(root, 0, 0)] if root is not None else []
        while stack:
            node, row, column = stack.pop()
            nodes.append((column, row, node.val))
            if node.right is not None:
                stack.append((node.right, row + 1, column + 1))
            if node.left is not None:
                stack.append((node.left, row + 1, column - 1))
        answer = []
        previous = None
        for column, row, value in sorted(nodes):
            if column != previous:
                answer.append([])
                previous = column
            answer[-1].append(value)
        return answer
