# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T16:24:17Z
# Experiment: ai-leetcode-lab, round 1
from __future__ import annotations

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        current = head

        def build(size: int) -> Optional[TreeNode]:
            nonlocal current
            if size == 0:
                return None
            left = build(size // 2)
            root = TreeNode(current.val)
            current = current.next
            root.left = left
            root.right = build(size - size // 2 - 1)
            return root

        return build(length)
