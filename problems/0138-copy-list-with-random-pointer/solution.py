# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:26:41Z
# Experiment: ai-leetcode-lab, round 1
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head
        while current:
            copy = Node(current.val, current.next)
            current.next = copy
            current = copy.next

        current = head
        while current:
            copy = current.next
            copy.random = current.random.next if current.random else None
            current = copy.next

        dummy = Node(0)
        copy_tail = dummy
        current = head
        while current:
            copy = current.next
            current.next = copy.next
            copy_tail.next = copy
            copy_tail = copy
            current = current.next
        return dummy.next
