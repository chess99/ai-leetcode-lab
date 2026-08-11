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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previous = dummy
        current = head
        while current:
            if current.next and current.val == current.next.val:
                duplicate = current.val
                while current and current.val == duplicate:
                    current = current.next
                previous.next = current
            else:
                previous = current
                current = current.next
        return dummy.next
