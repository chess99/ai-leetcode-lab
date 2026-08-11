# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:46:15Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        banned = set(nums)
        dummy = ListNode(0, head)
        current = dummy
        while current.next:
            if current.next.val in banned:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next
