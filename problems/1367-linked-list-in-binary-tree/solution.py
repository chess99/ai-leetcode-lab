# AI solution attribution
# Client: Codex Desktop
# Model: gpt-5.6-terra
# Reasoning effort: medium
# Profile: terra-medium
# Created: 2026-08-11T18:43:07Z
# Experiment: ai-leetcode-lab, round 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def match(node, link):
            if not link: return True
            if not node or node.val != link.val: return False
            return match(node.left, link.next) or match(node.right, link.next)
        if not root: return False
        return match(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
