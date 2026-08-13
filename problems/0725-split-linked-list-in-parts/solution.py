# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:41:39Z
# Experiment: ai-leetcode-lab, round 1
# Definition for singly-linked list.
from typing import List, Optional


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, node = 0, head
        while node: length += 1; node = node.next
        base, extra = divmod(length, k); result = []
        for part in range(k):
            result.append(head); size = base + (part < extra)
            for _ in range(size - 1): head = head.next
            if head: head.next, head = None, head.next
        return result
