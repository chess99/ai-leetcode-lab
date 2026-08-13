# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:46:16Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummy = ListNode(0, head)
        size = 1
        while size < length:
            tail, current = dummy, dummy.next
            while current:
                left = current
                right = self._split(left, size)
                current = self._split(right, size)
                tail = self._merge(left, right, tail)
            size *= 2
        return dummy.next

    def _split(self, head: Optional[ListNode], size: int) -> Optional[ListNode]:
        if head is None:
            return None
        for _ in range(size - 1):
            if head.next is None:
                break
            head = head.next
        rest = head.next
        head.next = None
        return rest

    def _merge(self, left: Optional[ListNode], right: Optional[ListNode],
               tail: ListNode) -> ListNode:
        while left and right:
            if left.val <= right.val:
                tail.next, left = left, left.next
            else:
                tail.next, right = right, right.next
            tail = tail.next
        tail.next = left or right
        while tail.next:
            tail = tail.next
        return tail
