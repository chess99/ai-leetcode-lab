# AI solution attribution
from typing import Optional
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:04Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional["TreeNode"]) -> int:
        if root is None:
            return 0
        cameras = 0
        states = {}
        stack = [(root, False)]
        while stack:
            node, processed = stack.pop()
            if not processed:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))
                continue
            left = states.get(node.left, 1)
            right = states.get(node.right, 1)
            if left == 2 or right == 2:
                cameras += 1
                states[node] = 0
            elif left == 0 or right == 0:
                states[node] = 1
            else:
                states[node] = 2
        if states[root] == 2:
            cameras += 1
        return cameras
