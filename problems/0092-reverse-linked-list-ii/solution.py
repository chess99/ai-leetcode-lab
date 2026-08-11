# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:18:29Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional


class Solution:
    def reverseBetween(self, head: Optional["ListNode"], left: int, right: int) -> Optional["ListNode"]:
        dummy = ListNode(0, head)
        before = dummy
        for _ in range(left - 1):
            before = before.next

        current = before.next
        for _ in range(right - left):
            moved = current.next
            current.next = moved.next
            moved.next = before.next
            before.next = moved
        return dummy.next
