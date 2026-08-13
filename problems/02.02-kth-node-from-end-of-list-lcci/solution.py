# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:54:54Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations

from typing import Optional


class Solution:
    def kthToLast(self, head: Optional[ListNode], k: int) -> int:
        fast = slow = head
        for _ in range(k):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow.val
