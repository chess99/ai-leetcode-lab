# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:03:06Z
# Experiment: ai-leetcode-lab, round 1
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Node:
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val, self.prev, self.next, self.child = val, prev, next, child

from typing import Optional

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        stack = [head]
        previous = None
        while stack:
            node = stack.pop()
            if previous is not None:
                previous.next = node
                node.prev = previous
            if node.next is not None:
                stack.append(node.next)
            if node.child is not None:
                stack.append(node.child)
                node.child = None
            previous = node
        head.prev = None
        return head
