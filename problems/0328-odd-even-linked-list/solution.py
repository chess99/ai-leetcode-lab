# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:47:40Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional


class Solution:
    def oddEvenList(self, head: Optional["ListNode"]) -> Optional["ListNode"]:
        if not head or not head.next:
            return head
        odd, even = head, head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head
