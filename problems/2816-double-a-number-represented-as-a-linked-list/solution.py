# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T21:23:05Z
# Experiment: ai-leetcode-lab, round 1
from typing import Optional




class Solution:
    def doubleIt(self, head: Optional['ListNode']) -> Optional['ListNode']:
        if head.val >= 5:
            head = ListNode(0, head)
        node = head
        while node:
            node.val = (node.val * 2 + (node.next.val >= 5 if node.next else 0)) % 10
            node = node.next
        return head
