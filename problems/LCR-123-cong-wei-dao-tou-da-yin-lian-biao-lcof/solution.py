# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:39:38Z
# Experiment: ai-leetcode-lab, round 1
from typing import List, Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBookList(self, head: Optional[ListNode]) -> List[int]:
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result[::-1]
