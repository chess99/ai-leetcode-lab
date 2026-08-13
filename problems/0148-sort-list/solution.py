# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:27:12Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional

# Definition for singly-linked list.
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        def split(start: Optional[ListNode], size: int) -> Optional[ListNode]:
            if start is None:
                return None
            for _ in range(size - 1):
                if start.next is None:
                    return None
                start = start.next
            next_start = start.next
            start.next = None
            return next_start

        def merge(left: Optional[ListNode], right: Optional[ListNode]):
            merged_dummy = ListNode()
            tail = merged_dummy
            while left and right:
                if left.val <= right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next
            tail.next = left or right
            while tail.next:
                tail = tail.next
            return merged_dummy.next, tail

        dummy = ListNode(0, head)
        size = 1
        while size < length:
            previous = dummy
            current = dummy.next
            while current:
                left = current
                right = split(left, size)
                current = split(right, size)
                merged_head, merged_tail = merge(left, right)
                previous.next = merged_head
                previous = merged_tail
            size *= 2
        return dummy.next
