# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:12:21Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        answer = 0
        stack = [(root, root.val, root.val)]
        while stack:
            node, smallest, largest = stack.pop()
            answer = max(answer, largest - node.val, node.val - smallest)
            smallest = min(smallest, node.val)
            largest = max(largest, node.val)
            if node.left:
                stack.append((node.left, smallest, largest))
            if node.right:
                stack.append((node.right, smallest, largest))
        return answer
