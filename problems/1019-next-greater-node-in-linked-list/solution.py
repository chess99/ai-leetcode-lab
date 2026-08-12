# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:10:48Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values=[]
        while head: values.append(head.val);head=head.next
        result=[0]*len(values);stack=[]
        for i,value in enumerate(values):
            while stack and values[stack[-1]]<value: result[stack.pop()]=value
            stack.append(i)
        return result
