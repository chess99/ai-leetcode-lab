# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:24:52Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previous_group = dummy
        while True:
            group_end = previous_group
            for _ in range(k):
                group_end = group_end.next
                if not group_end:
                    return dummy.next
            next_group = group_end.next
            previous, current = next_group, previous_group.next
            while current != next_group:
                following = current.next
                current.next = previous
                previous = current
                current = following
            old_start = previous_group.next
            previous_group.next = group_end
            previous_group = old_start
