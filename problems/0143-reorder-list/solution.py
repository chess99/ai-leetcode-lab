# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:26:41Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        previous = None
        while second:
            next_node = second.next
            second.next = previous
            previous = second
            second = next_node

        first, second = head, previous
        while second:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next
            first, second = first_next, second_next
