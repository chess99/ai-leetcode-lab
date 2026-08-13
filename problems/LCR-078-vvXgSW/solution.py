# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T18:34:25Z
# Experiment: ai-leetcode-lab, round 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappop, heappush
from typing import List


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        serial = 0
        for node in lists:
            if node is not None:
                heappush(heap, (node.val, serial, node))
                serial += 1
        dummy = tail = type(lists[0])(0) if lists and lists[0] is not None else None
        if dummy is None:
            if not heap:
                return None
            node_type = type(heap[0][2])
            dummy = tail = node_type(0)
        while heap:
            _, _, node = heappop(heap)
            tail.next = node
            tail = node
            if node.next is not None:
                heappush(heap, (node.next.val, serial, node.next))
                serial += 1
        return dummy.next
