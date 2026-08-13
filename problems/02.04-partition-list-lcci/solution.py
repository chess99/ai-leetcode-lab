# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:48Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller_dummy = ListNode()
        larger_dummy = ListNode()
        smaller, larger = smaller_dummy, larger_dummy
        while head:
            following = head.next
            head.next = None
            if head.val < x:
                smaller.next = head
                smaller = head
            else:
                larger.next = head
                larger = head
            head = following
        smaller.next = larger_dummy.next
        return smaller_dummy.next
