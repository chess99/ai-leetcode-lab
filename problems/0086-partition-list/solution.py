# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:17:37Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        smaller_tail, greater_tail = smaller_dummy, greater_dummy
        current = head
        while current:
            next_node = current.next
            current.next = None
            if current.val < x:
                smaller_tail.next = current
                smaller_tail = current
            else:
                greater_tail.next = current
                greater_tail = current
            current = next_node
        smaller_tail.next = greater_dummy.next
        return smaller_dummy.next
