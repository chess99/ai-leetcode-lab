# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T04:15:26Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        first, second = [], []
        while l1:
            first.append(l1.val)
            l1 = l1.next
        while l2:
            second.append(l2.val)
            l2 = l2.next
        carry = 0
        head = None
        while first or second or carry:
            total = carry
            if first:
                total += first.pop()
            if second:
                total += second.pop()
            head = ListNode(total % 10, head)
            carry = total // 10
        return head
