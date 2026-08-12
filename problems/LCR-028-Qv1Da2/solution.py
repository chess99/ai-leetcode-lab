# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:27Z
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

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        stack = [head]
        previous = None
        while stack:
            node = stack.pop()
            if previous:
                previous.next = node
                node.prev = previous
            if node.next:
                stack.append(node.next)
            if node.child:
                stack.append(node.child)
                node.child = None
            previous = node
        return head
