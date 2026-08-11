# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T20:05:21Z
# Experiment: ai-leetcode-lab, round 1
class Solution:
    def reverseEvenLengthGroups(self, head):
        if not head:
            return head

        previous = head
        expected_length = 2

        while previous.next:
            group_start = previous.next
            group_end = group_start
            actual_length = 1
            while actual_length < expected_length and group_end.next:
                group_end = group_end.next
                actual_length += 1
            after_group = group_end.next

            if actual_length % 2 == 0:
                node = group_start
                reversed_head = after_group
                while node != after_group:
                    next_node = node.next
                    node.next = reversed_head
                    reversed_head = node
                    node = next_node
                previous.next = reversed_head
                previous = group_start
            else:
                previous = group_end

            expected_length += 1

        return head
