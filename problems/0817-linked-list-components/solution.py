# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T17:48:18Z
# Experiment: ai-leetcode-lab, round 1
# Definition for singly-linked list.
from typing import List, Optional
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        values, count = set(nums), 0
        while head:
            if head.val in values and (head.next is None or head.next.val not in values): count += 1
            head = head.next
        return count
