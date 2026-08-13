# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:23Z
# Experiment: ai-leetcode-lab, round 1

from typing import Optional


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        previous = None
        slow = head
        fast = head
        while fast and fast.next:
            previous = slow
            slow = slow.next
            fast = fast.next.next

        previous.next = slow.next
        return head
