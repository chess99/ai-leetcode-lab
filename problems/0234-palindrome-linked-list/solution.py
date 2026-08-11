# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T10:28:18Z
# Experiment: ai-leetcode-lab, round 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next

        previous = None
        while slow:
            following = slow.next
            slow.next = previous
            previous = slow
            slow = following

        left, right = head, previous
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
