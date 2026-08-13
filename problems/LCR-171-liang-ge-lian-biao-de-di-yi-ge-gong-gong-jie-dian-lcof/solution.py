# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:45:39Z
# Experiment: ai-leetcode-lab, round 1

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        left, right = headA, headB
        while left is not right:
            left = left.next if left else headB
            right = right.next if right else headA
        return left
