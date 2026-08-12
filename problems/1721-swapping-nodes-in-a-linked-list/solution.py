# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T19:16:33Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        first = head
        for _ in range(k - 1):
            first = first.next

        second = head
        runner = first
        while runner.next:
            runner = runner.next
            second = second.next

        first.val, second.val = second.val, first.val
        return head
