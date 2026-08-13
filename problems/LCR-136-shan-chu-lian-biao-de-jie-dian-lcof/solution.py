# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:41:25Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNode(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head.val == val:
            return head.next
        current = head
        while current.next and current.next.val != val:
            current = current.next
        if current.next:
            current.next = current.next.next
        return head
