# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:26Z
# Experiment: ai-leetcode-lab, round 1

from typing import Optional


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        previous = None
        while slow:
            following = slow.next
            slow.next = previous
            previous = slow
            slow = following

        answer = 0
        first_half = head
        second_half = previous
        while second_half:
            answer = max(answer, first_half.val + second_half.val)
            first_half = first_half.next
            second_half = second_half.next

        return answer
