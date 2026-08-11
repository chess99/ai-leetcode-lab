# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:26:24Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        last = {}
        prefix = 0
        node = dummy
        while node:
            prefix += node.val
            last[prefix] = node
            node = node.next

        prefix = 0
        node = dummy
        while node:
            prefix += node.val
            node.next = last[prefix].next
            node = node.next
        return dummy.next
