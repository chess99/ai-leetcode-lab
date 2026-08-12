# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:27:11Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = head
        while current:
            next_node = current.next
            previous = dummy
            while previous.next and previous.next.val <= current.val:
                previous = previous.next
            current.next = previous.next
            previous.next = current
            current = next_node
        return dummy.next
