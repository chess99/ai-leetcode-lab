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
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if not head:
            node.next = node
            return node
        current = head
        while True:
            following = current.next
            normal = current.val <= insertVal <= following.val
            turning = current.val > following.val and (insertVal >= current.val or insertVal <= following.val)
            if normal or turning or following is head:
                current.next = node
                node.next = following
                return head
            current = following
