# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:36Z
# Experiment: ai-leetcode-lab, round 1
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return None
        stack, current, first, previous = [], root, None, None
        while stack or current:
            while current: stack.append(current); current = current.left
            current = stack.pop()
            if previous: previous.right = current; current.left = previous
            else: first = current
            previous = current; current = current.right
        first.left = previous; previous.right = first
        return first
