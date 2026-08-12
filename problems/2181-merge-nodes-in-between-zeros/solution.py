# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:31Z
# Experiment: ai-leetcode-lab, round 1

from __future__ import annotations

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        total = 0
        node = head.next

        while node:
            if node.val == 0:
                tail.next = ListNode(total)
                tail = tail.next
                total = 0
            else:
                total += node.val
            node = node.next

        return dummy.next
