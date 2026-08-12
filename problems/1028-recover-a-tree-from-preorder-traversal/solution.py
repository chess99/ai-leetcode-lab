# AI solution attribution
from typing import Optional
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T06:20:07Z
# Experiment: ai-leetcode-lab, round 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional["TreeNode"]:
        stack = []
        index = 0
        while index < len(traversal):
            depth = 0
            while traversal[index] == '-':
                depth += 1
                index += 1
            start = index
            while index < len(traversal) and traversal[index].isdigit():
                index += 1
            node = TreeNode(int(traversal[start:index]))
            while len(stack) > depth:
                stack.pop()
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)
        return stack[0]
