# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:08:06Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional


class Solution:
    def swapPairs(self, head: Optional["ListNode"]) -> Optional["ListNode"]:
        dummy = ListNode(0, head)
        previous = dummy
        while previous.next and previous.next.next:
            first = previous.next
            second = first.next
            first.next = second.next
            second.next = first
            previous.next = second
            previous = first
        return dummy.next
