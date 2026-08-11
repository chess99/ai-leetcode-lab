# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T15:54:54Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def removeDuplicateNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        previous = None
        current = head
        while current:
            if current.val in seen:
                previous.next = current.next
            else:
                seen.add(current.val)
                previous = current
            current = current.next
        return head
