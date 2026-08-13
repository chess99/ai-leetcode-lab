# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-12T05:00:50Z
# Experiment: ai-leetcode-lab, round 1

from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def listOfDepth(self, tree: Optional[TreeNode]) -> List[Optional[ListNode]]:
        if not tree:
            return []
        answer = []
        queue = deque([tree])
        while queue:
            dummy = ListNode()
            tail = dummy
            for _ in range(len(queue)):
                node = queue.popleft()
                tail.next = ListNode(node.val)
                tail = tail.next
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            answer.append(dummy.next)
        return answer
