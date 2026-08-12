# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:24:52Z
# Experiment: ai-leetcode-lab, round 1
from typing import List, Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        heap = []
        for index, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, index, node))
        dummy = ListNode()
        tail = dummy
        while heap:
            _, index, node = heapq.heappop(heap)
            tail.next = node
            tail = node
            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))
        tail.next = None
        return dummy.next
